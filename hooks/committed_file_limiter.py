#!/usr/bin/env python
# Pre-commit git hook intended to check the size of files in the
# index to prevent large files from being committed
# Don't forget to like and Subscribe at the Gitschooldude Youtube
# Channel: https://www.youtube.com/channel/UCshmCws1MijkZLMkPmOmzbQ
# Edits to limits and file types should be made in the main() function

# Copyright (C) [2019] by [Dan Gitschooldude] <[gitschooldude@gmail.com]> 
# Permission to use, copy,
# modify, and/or distribute this software for any purpose with or without fee is
# hereby granted.  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
# RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE
# USE OR PERFORMANCE OF THIS SOFTWARE.

# If there's an issue with imports we want to make sure this fails in a way
# that will not block a commit from being possible. Nothing will piss off
# your developers more than blocking their commits because of your mistake!
try:
  import os, sys, warnings, inspect, pdb
  # this_file will show up as .git/hooks/pre-commit or 
  # hooks/committed_file_limiter.py depending on whether git runs this
  # or I run it in testing.  We need this_file to be the latter
  this_file = os.path.abspath(inspect.getfile(inspect.currentframe()))
  if '.git/hooks' in this_file:
     this_file = os.path.realpath(this_file)
  sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(this_file), '../external/GitPython')))
  import git
except Exception as e:
    print("WARNING: Issue running pre-commit hook %s " % this_file)
    print(str(e))
    print("  Skipping hook and continuing to commit message...")
    sys.exit(0)

class CommittedFileLimiter():
    def __init__(self, ignore_merge_commits=True, absolute_max=5.0,
          filter=["modified", "added", "renamed", "deleted"]):
        self._top = os.path.abspath( os.path.join(
          os.path.dirname(this_file), ".."))
        self._ignore_merge_commits = ignore_merge_commits
        self._absolute_max = absolute_max
        self._filter = filter
        self._file_size_limits = {} # extension : file size limit map

    def _get_index_files(self):
        """
        Returns a list of file paths which are about to be committed, filtered
        by _filter
        """
        repo = git.Repo(self._top)
        index = repo.index

        files_in_index = []
        # Get diff representing what's in index vs HEAD
        diff = repo.index.diff(repo.commit('HEAD'))

        # NOTE 'A' for 'added' is actually 'deleted' and
        #      'D' for 'deleted' is actually 'added'
        #      Think of it in diff terms: | index | HEAD |
        if "modified" in self._filter:
            for d in diff.iter_change_type('M'):
                files_in_index.append(str(d.b_blob.path))

        if "deleted" in self._filter:
            for d in diff.iter_change_type('A'):
                try:
                    files_in_index.append(str(d.b_blob.path))
                    files_in_index.append(str(d.a_blob.path))
                except:
                    pass

        if "added" in self._filter:
            for d in diff.iter_change_type('D'):
                try:
                    files_in_index.append(str(d.a_blob.path))
                    files_in_index.append(str(d.b_blob.path))
                except:
                    pass

        if "renamed" in self._filter:
            for d in diff.iter_change_type('R'):
                try:
                    files_in_index.append(str(d.b_blob.path))
                    files_in_index.append(str(d.a_blob.path))
                except:
                    pass

        return files_in_index

    def add_limit(self, extensions, size_in_mb):
        for ext in extensions:
            try:
                size_in_mb = float(size_in_mb)
            except:
                print("WARNING: Couldn't add %d to file size limits definition,"
                  " error converting to a float! Ignoring this one." % size_in_mb)
                return
            # Overwrite existing extension data if necessary
            self._file_size_limits[ext] = size_in_mb

    def can_be_committed(self):
        """
        Evaluates file size limits to determine if commit is possible
        returns True/False if commit is possible and Reason(s)
        """
        value = True
        reason = ''

        if self._ignore_merge_commits:
            # If this is the index of a soon-to-be merge commit, bail!
            if os.path.isfile(os.path.join(self._top, '.git/MERGE_HEAD')):
                value = True
                reason = 'Merge commit exempt from check.'
                return value, reason

        files_in_index = self._get_index_files()

        # Store off cwd so we can cd back to it after this process
        prev_dir = os.getcwd()
        # cd to top level so our file stats have the right path
        os.chdir(self._top)
        # Get the sizes of all files in the index
        filesizes = {}
        for file in files_in_index:
            filesizes[file]= self._getsize(file.strip())

        for file in filesizes:
            filesize = filesizes[file]
            basename = os.path.basename(file)
            filename, extension = os.path.splitext(basename)

            # Check file size limit for this file extension or absolute_max
            if float(filesize) > self._to_bytes(self._absolute_max):  # convert to bytes!
                value = False
                reason += ("\nFile %-20s %-20s  found in index is larger than "
                    "the absolute max: %-2.2f MB." % 
                    (file, "(%d bytes)" % filesize, self._absolute_max))
            elif extension in self._file_size_limits:
                if float(filesize) > self._to_bytes(float(self._file_size_limits[extension])):
                    value = False
                    reason += ("\nFile %-20s %-20s  found in index is larger than "
                        "the limit for extension %-5s: %-2.2f MB." %
                        (file, "(%d bytes)" % filesize, extension, self._file_size_limits[extension]))

        os.chdir(prev_dir)  # Go back to wherever we were
        return value, reason

    def _to_bytes(self, mb):
        return(mb*2 **20)

    def _getsize(self, f):
        """
        Get the size of a file, wrapped in try in the event the file has
        been removed or renamed
        TODO: Index file sizes are assumed identical to file size on disk
              which is a poor assumption. Should really ask for that information
              via GitPython but I'm not even getting paid to write this so
              who cares! - Gitschooldude
        """
        try:
            return os.path.getsize(f)
        except (EnvironmentError, OSError):
            return 0

def main():
  try:
    cfl = CommittedFileLimiter(
      ignore_merge_commits=True,
      absolute_max=5.0)

    # Add limits to particular file extensions of the form
    # [list of file extensions], <size in MB for those extensions>
    cfl.add_limit(['.cpp', '.cc', '.c'],  1.0)
    cfl.add_limit(['.hpp', '.hh', '.h'],   0.5)
    cfl.add_limit(['.pdf', '.doc', '.xls'],  0.5)
    cfl.add_limit(['.png'],  0.2)

    print("Looking for files that are too large in the index...")
    can_be_committed, reason = cfl.can_be_committed()
    if can_be_committed:
        print("All files pass size check. Continuing to commit message...")
    else:
        print("Refusing to commit due to file size limits:")
        print(reason)
        sys.exit(1)

    sys.exit(0)
  # If there's an issue of any kind we want to make sure this fails in a way
  # that will not block a commit from being possible
  except Exception as e:
    print("WARNING: Issue running pre-commit hook %s " % this_file)
    print(str(e))
    print("  Skipping hook and continuing to commit message...")
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main())
