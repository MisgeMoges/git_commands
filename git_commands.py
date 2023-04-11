# Clone the remote repository to your local machine
git clone https://github.com/team/repository.git

# Check the status of your local repository
git status

# Create a new branch and switch to it
git checkout -b new-feature

# Make changes to files in the new-feature branch
# ...

# Add the changes to the staging area
git add .

# Commit the changes to the new-feature branch
git commit -m "Added a new feature"

# Push the new-feature branch to the remote repository
git push origin new-feature

# Switch back to the main branch
git checkout main

# Update your local repository with the latest changes from the remote repository
git pull origin main

# Merge the changes from the new-feature branch into the main branch
git merge new-feature

# Delete the new-feature branch
git branch -d new-feature

# Create a tag for a specific commit
git tag v1.0.0 <commit-hash>

# View the commit history of your local repository
git log

# View the differences between two versions of a file
git diff <commit-hash-1> <commit-hash-2>

# Temporarily store changes that are not ready to be committed
git stash

# Undo changes that have been committed or staged
git reset --hard HEAD

# Apply changes from a specific commit
git cherry-pick <commit-hash>

# View the author and date of each line in a file
git blame file.txt

# Download new changes from the remote repository without merging them into your local repository
git fetch origin

# Manage submodules
git submodule add https://github.com/team/submodule.git
git submodule init
git submodule update
