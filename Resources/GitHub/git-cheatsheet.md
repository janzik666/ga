# Git Cheatsheet

## Saving your changes
Make sure you are on YOUR OWN branch, NOT on the main branch.
1. `git add .` This adds all your current changes to staging
2. `git commit -m "COMMIT MESSAGE"` This commits your changes (but they remain on your local machine)
3. `git push origin <YOUR BRANCH NAME>` This will actually push your commits to your branch on GitHub


## Pulling down changes from the main branch
Make sure all your own changes have been committed and pushed.
1. `git checkout <MAIN BRANCH NAME>` This switches your current branch to the main one on your local machine
2. `git pull origin <MAIN BRANCH NAME>` This pulls down all the latest changes from the main branch on GitHub
3. `git chekcout <YOUR BRANCH NAME>` We've now switched back into your branch
4. `git merge <MAIN BRANCH NAME>` This will attempt to merge all the latest changes from the main branch into your branch
Note: The last step will open a git commit message in your command line with a pre-written commit message. All you have to do is close and save that file and you will be all set.

## Creating a brand new branch
1. `git checkout -b <YOUR NEW BRANCH NAME>`