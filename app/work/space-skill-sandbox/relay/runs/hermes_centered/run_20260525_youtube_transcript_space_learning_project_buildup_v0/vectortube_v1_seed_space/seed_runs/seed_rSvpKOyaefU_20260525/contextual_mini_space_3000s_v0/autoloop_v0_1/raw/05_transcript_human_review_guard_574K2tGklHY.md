0:00 Pre-commit hooks. Running checks before
0:02 committing changes in software
0:04 development. Ensuring code quality and
0:07 consistency is crucial. One effective
0:09 way to achieve this is by using
0:11 pre-commit hooks. These hooks are
0:14 automated checks that run before you
0:15 commit your code, helping you catch
0:18 issues early and maintain a high
0:20 standard of code
0:22 quality. What are pre-commit hooks?
0:25 Pre-commit hooks are scripts that run
0:27 automatically before a commit is
0:29 completed in Git. They allow you to
0:32 inspect the changes that are about to be
0:34 committed and can prevent the commit if
0:36 certain conditions aren't met. The
0:38 purpose of pre-commit hooks are to catch
0:40 issues early in development, enforce
0:42 code quality standards, prevent
0:44 problematic code from entering the
0:46 repository, automate repetitive checks,
0:49 and maintain consistency across team
0:51 members.
0:54 How do pre-commit hooks work? First, a
0:57 developer adds files to the staging area
0:59 with the command git add. Then, a
1:02 developer runs git commit to save
1:04 changes, initiating the commit process.
1:08 Pre-commit hooks then run automatically
1:10 to check the code. Finally, the commit
1:12 proceeds or is blocked based on the hook
1:15 results. This ensures that only code
1:17 that meets the defined standards is
1:19 committed to the repository.
1:23 Here are some common use cases for
1:25 pre-commit hooks. Code linting enforces
1:28 coding style and catches syntax errors
1:30 using tools like ESLint, Pyint or
1:34 Rubocop. Unit testing runs tests to
1:36 ensure code changes don't break existing
1:39 functionality. Code formatting
1:41 automatically formats code using tools
1:43 like prettier, black, or god. Security
1:47 scanning checks for security
1:49 vulnerabilities, secrets or credentials
1:51 in code. Code complexity analyzes and
1:54 limits code complexity to maintain
1:57 maintainability. Finally, pre-commit
1:59 hooks can prevent commits to protected
2:01 branches or with specific patterns like
2:04 to-do
2:06 comments. Let's discuss setting up
2:08 pre-commit hooks. For manual setup,
2:12 first create agit/hooks directory in
2:15 your
2:15 repository. Next, create a file named
2:18 pre-commit with no extension. Then make
2:22 the file executable with the command
2:24 schmod plus x. Write your script using
2:27 bash, python, or any executable
2:30 language. Finally, test your hook by
2:32 making a commit. Here's a basic
2:35 pre-commit hook example. The script
2:38 starts with a shebang line specifying
2:40 that it should be executed with bash. It
2:43 then echoes which means prints running
2:45 pre-commit hook. The script checks for
2:48 console.log statements in JavaScript
2:50 files, uses git diff to find change
2:54 files and then uses gp to search for
2:56 console.log statements. If console.log
3:00 is found, it prints an error message and
3:02 exits with code one which indicates
3:05 failure. Otherwise, it exits with code
3:08 zero indicating
3:11 success. An easier way to set up
3:13 pre-commit hooks is by using the
3:15 pre-commit framework. The pre-commit
3:17 framework is a Python package that
3:19 simplifies managing and maintaining
3:21 pre-commit hooks. It provides a
3:24 collection of readytouse hooks and makes
3:26 it easy to share hooks across projects.
3:29 To use it, first install pre-commit
3:32 using the command pip install
3:34 pre-commit.
3:35 Next, create a file named pre-commit
3:40 config.yaml. Then install hooks by
3:42 running the command pre-commit install.
3:45 Finally, commit changes as usual. Here's
3:48 a sample configuration file. Under
3:51 repos, it specifies three repositories.
3:55 Pre-commit/precommit hooks,
3:57 psf/black, and pick a/flake 8. For each
4:02 repository, it defines a set of hooks to
4:04 run such as trailing whites space, end
4:07 of file fixer, check yaml, black, and
4:11 flake
4:13 8. Let's see how to create custom
4:16 pre-commit hooks. When built-in hooks
4:18 don't meet your needs, you can create
4:20 custom hooks tailored to your project
4:23 requirements. First, script should be
4:25 executable and have a shebang line.
4:28 Next, return exit code zero for success.
4:31 non-zero for failure. Keep hooks focused
4:34 on a single
4:35 responsibility. Include clear error
4:37 messages for failures. Test hooks
4:40 thoroughly before
4:41 deployment. And finally, document hook
4:44 behavior for team members. Here's how to
4:47 use a custom hook in the pre-commit
4:49 framework. Here, a local repository is
4:52 defined and a hook named forbidden words
4:55 is set up to check for forbidden words
4:57 like to-do or fem. The hook is
5:00 implemented in the file
5:02 check_forbidden_words py uses Python and
5:05 applies to text files excluding files in
5:08 the.getit directory. This configuration
5:11 ensures that the custom hook runs during
5:13 the commit
5:16 stage. Here are some best practices for
5:19 pre-commit hooks. Keep hooks fast. So
5:22 optimize hooks for speed to avoid
5:24 disrupting workflow. Run comprehensive
5:27 tests in continuous integration and
5:29 continuous delivery pipelines instead of
5:31 pre-commit hooks. Use version control
5:34 for your hooks, storing hook
5:36 configurations in version control to
5:38 ensure consistency across all team
5:40 members and
5:41 environments. Focus on specific issues.
5:44 Design hooks to catch specific problems
5:47 rather than trying to solve everything.
5:49 Each hook should have a clear single
5:52 responsibility. Finally, provide bypass
5:54 options.
5:56 Allow developers to bypass hooks in
5:58 exceptional cases using the command git
6:00 commit double- no-verify, but log these
6:05 exceptions. In summary, pre-commit hooks
6:08 automate code quality checks before
6:10 changes are committed. They help catch
6:12 issues early in the development process.
6:15 They can be set up manually or using
6:17 frameworks like pre-commit. Pre-commit
6:20 hooks enforce consistent standards
6:22 across team members. For further
6:25 resources, you can visit
6:26 precommit.com,
6:29 gsecm.com/doccks/gith hooks, and
6:33 github.com/precommit/precommit
6:35 hooks. If you like this video, hit that
6:38 like button and don't forget to
6:41 subscribe. Visit codelucky.com for more
6:44 such useful content.
6:46 [Music]