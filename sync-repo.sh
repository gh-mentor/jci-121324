# This bash script uses git to synchronize changes between the local and remote GitHub repository on branch 'main'.

# Steps: pull changes from remote repository, stage all changes, commit changes with message 'Updated', push changes to remote repository on branch 'main'.

# Pull changes from remote repository
git pull origin main

# Stage all changes
git stage .

# Commit changes with message 'Updated'
git commit -m "Updated"

# Push changes to remote repository on branch 'main'
git push origin main

# Echo message to indicate that the script has finished running
echo "Script has finished running"