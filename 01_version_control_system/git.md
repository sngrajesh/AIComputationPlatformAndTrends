## Git Notes

## Table of Contents
1. [Initial Setup](#initial-setup)
   - [Installing Git](#installing-git)
   - [Git Configuration](#git-configuration)
2. [Creating and Cloning Repositories](#creating-and-cloning-repositories)
3. [Working with Files](#working-with-files)
4. [Branching and Merging](#branching-and-merging)
5. [Remote Repositories](#remote-repositories)
6. [Viewing History](#viewing-history)
7. [Stashing Changes](#stashing-changes)
8. [Tags](#tags)
9. [Undoing Changes](#undoing-changes)
10. [Submodules](#submodules)
11. [Miscellaneous](#miscellaneous)
12. [Visual Studio Code Git Interface](#visual-studio-code-git-interface)
    - [Source Control Panel Features](#source-control-panel-features)
    - [Useful VSCode Git Commands](#useful-vscode-git-commands-command-palette)
13. [Advanced Operations](#advanced-operations)
    - [Stashing Changes](#stashing-changes-1)
    - [Reverting Changes](#reverting-changes)
    - [Resolving Merge Conflicts](#resolving-merge-conflicts)
14. [Best Practices](#best-practices)
    - [Commit Messages](#commit-messages)
    - [Branching Strategy](#branching-strategy)
    - [Regular Operations](#regular-operations)
15. [Troubleshooting Common Issues](#troubleshooting-common-issues)
16. [Example](#example)


---

### Initial Setup

#### Installing Git
1. Download Git from [git-scm.com](https://git-scm.com)
2. Install Git with recommended settings
3. Verify installation: 
```bash
git --version
```

#### Git Configuration
```bash
### Set user name and email
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

## Set default branch name
git config --global init.defaultBranch main

### Check configuration
git config --list
```

#### Creating and Cloning Repositories
```bash
### Initialize a new Git repository
git init

### Clone an existing repository
git clone <repository-url>
```

#### Working with Files
```bash
### Check the status of your working directory
git status

### Add files to the staging area
git add <file>

### Add all files to the staging area
git add .

### Commit changes
git commit -m "Commit message"

### Remove files from the repository
git rm <file>
```

#### Branching and Merging
```bash
### Create a new branch
git branch <branch-name>

### List all branches
git branch

### Switch to a branch
git checkout <branch-name>

### Create and switch to a new branch
git checkout -b <branch-name>

### Merge a branch into the current branch
git merge <branch-name>

### Delete a branch
git branch -d <branch-name>
```

#### Remote Repositories
```bash
### Add a remote repository
git remote add <name> <repository-url>

### List remote repositories
git remote -v

### Remove a remote repository
git remote remove <name>

### Fetch changes from a remote repository
git fetch <remote>

### Pull changes from a remote repository
git pull <remote> <branch>

### Push changes to a remote repository
git push <remote> <branch>
```

#### Viewing History
```bash
### Show commit history
git log

### Show commit history with a graph
git log --oneline --graph --all

### Show changes in a commit
git show <commit-hash>

### Show changes between commits
git diff <commit-hash1> <commit-hash2>

### Show changes not staged for commit
git diff

### Show changes staged for commit
git diff --staged
```

#### Stashing Changes
```bash
### Stash changes
git stash

### List stashes
git stash list

### Apply the latest stash
git stash apply

### Apply a specific stash
git stash apply stash@{index}

### Drop a stash
git stash drop stash@{index}
```

#### Tags
```bash
### Create a new tag
git tag <tag-name>

### List all tags
git tag

### Push a tag to a remote repository
git push <remote> <tag-name>

### Delete a tag locally
git tag -d <tag-name>

### Delete a tag from a remote repository
git push <remote> --delete <tag-name>
```

#### Undoing Changes
```bash
### Unstage a file
git reset <file>

### Reset the staging area and working directory
git reset --hard <commit-hash>

### Revert a commit
git revert <commit-hash>
```

#### Submodules
```bash
### Add a submodule
git submodule add <repository-url>

### Update all submodules
git submodule update --init --recursive

### Remove a submodule
git submodule deinit -f <path-to-submodule>
rm -rf .git/modules/<path-to-submodule>
rm -rf <path-to-submodule>
```

#### Miscellaneous
```bash
### Show Git help
git help

### Show Git version
git --version

### Clean untracked files
git clean -f

### Create a .gitignore file
echo "*.log" >> .gitignore
git add .gitignore
git commit -m "Add .gitignore"
```

### Visual Studio Code Git Interface

#### Source Control Panel Features
1. Changes
   - Modified files show with M
   - New files show with U
   - Deleted files show with D
   - Click + to stage changes
   - Click - to unstage changes

2. Commit Area
   - Type commit message
   - Ctrl+Enter (Cmd+Enter on Mac) to commit
   - Three dots (...) menu for more options

3. Branch Management
   - Current branch shown in bottom left
   - Click to switch/create branches
   - Create branch from command palette: Ctrl+Shift+P > Git: Create Branch

#### Useful VSCode Git Commands (Command Palette)
- Git: `Clone`
- Git: `Initialize Repository`
- Git: `Create Branch`
- Git: `Checkout to`
- Git: `Pull`
- Git: `Push`
- Git: `Sync`
- Git: `Stage Changes`
- Git: `Unstage Changes`
- Git: `Commit`
- Git: `Publish Branch`

### Advanced Operations

#### Stashing Changes
```bash
## Stash current changes
git stash

## List stashes
git stash list

## Apply most recent stash
git stash pop

## Apply specific stash
git stash apply stash@{n}
```

#### Reverting Changes
```bash
## Revert last commit
git revert HEAD

## Revert specific commit
git revert <commit-hash>

## Reset to specific commit (careful!)
git reset --hard <commit-hash>
```

#### Resolving Merge Conflicts
1. Open conflicted file in VSCode
2. Look for conflict markers (<<<<<<, =======, >>>>>>>)
3. Choose which changes to keep
4. Stage resolved files
5. Commit the merge

### Best Practices

#### Commit Messages
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- First line should be 50 characters or less
- Add detailed description after blank line if needed

#### Branching Strategy
1. Main/Master branch: stable, production-ready code
2. Development branch: integration branch for features
3. Feature branches: individual features
4. Hotfix branches: urgent fixes for production

#### Regular Operations
1. Pull before starting new work
2. Create feature branch for new work
3. Make small, focused commits
4. Write clear commit messages
5. Pull and merge main branch regularly
6. Push changes frequently
 
 
#### Troubleshooting Common Issues
1. Merge Conflicts
   - Pull latest changes before merging
   - Communicate with team about overlapping work
   - Use VSCode's merge conflict resolver

2. Lost Changes
   - Use `git reflog` to find lost commits
   - Create branches before experimental changes
   - Commit frequently

3. Large Files
   - Use .gitignore for build artifacts
   - Consider Git LFS for large files
   - Keep repositories focused and minimal

Remember to regularly:
- Backup your repository
- Clean up old branches
- Review and update .gitignore
- Check repository health with `git status`



#### Example

<svg aria-roledescription="flowchart-v2" role="graphics-document document" viewBox="0 0 1208.390625 1409" style="max-width: 1208.390625px;" class="flowchart" xmlns="http://www.w3.org/2000/svg" width="100%" id="export-svg"><style xmlns="http://www.w3.org/1999/xhtml">@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"); p {margin: 0;}</style><style>#export-svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:14px;fill:#333;}#export-svg .error-icon{fill:#ffffff;}#export-svg .error-text{fill:#000000;stroke:#000000;}#export-svg .edge-thickness-normal{stroke-width:1px;}#export-svg .edge-thickness-thick{stroke-width:3.5px;}#export-svg .edge-pattern-solid{stroke-dasharray:0;}#export-svg .edge-thickness-invisible{stroke-width:0;fill:none;}#export-svg .edge-pattern-dashed{stroke-dasharray:3;}#export-svg .edge-pattern-dotted{stroke-dasharray:2;}#export-svg .marker{fill:#000000;stroke:#000000;}#export-svg .marker.cross{stroke:#000000;}#export-svg svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:14px;}#export-svg p{margin:0;}#export-svg .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#export-svg .cluster-label text{fill:#000000;}#export-svg .cluster-label span{color:#000000;}#export-svg .cluster-label span p{background-color:transparent;}#export-svg .label text,#export-svg span{fill:#333;color:#333;}#export-svg .node rect,#export-svg .node circle,#export-svg .node ellipse,#export-svg .node polygon,#export-svg .node path{fill:#ffffff;stroke:#000000;stroke-width:1px;}#export-svg .rough-node .label text,#export-svg .node .label text,#export-svg .image-shape .label,#export-svg .icon-shape .label{text-anchor:middle;}#export-svg .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#export-svg .rough-node .label,#export-svg .node .label,#export-svg .image-shape .label,#export-svg .icon-shape .label{text-align:center;}#export-svg .node.clickable{cursor:pointer;}#export-svg .root .anchor path{fill:#000000!important;stroke-width:0;stroke:#000000;}#export-svg .arrowheadPath{fill:#000000;}#export-svg .edgePath .path{stroke:#000000;stroke-width:2.0px;}#export-svg .flowchart-link{stroke:#000000;fill:none;}#export-svg .edgeLabel{background-color:hsl(-120, 0%, 80%);text-align:center;}#export-svg .edgeLabel p{background-color:hsl(-120, 0%, 80%);}#export-svg .edgeLabel rect{opacity:0.5;background-color:hsl(-120, 0%, 80%);fill:hsl(-120, 0%, 80%);}#export-svg .labelBkg{background-color:rgba(204, 204, 204, 0.5);}#export-svg .cluster rect{fill:#ffffff;stroke:hsl(0, 0%, 90%);stroke-width:1px;}#export-svg .cluster text{fill:#000000;}#export-svg .cluster span{color:#000000;}#export-svg div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:#ffffff;border:1px solid hsl(0, 0%, 90%);border-radius:2px;pointer-events:none;z-index:100;}#export-svg .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#export-svg rect.text{fill:none;stroke-width:0;}#export-svg .icon-shape,#export-svg .image-shape{background-color:hsl(-120, 0%, 80%);text-align:center;}#export-svg .icon-shape p,#export-svg .image-shape p{background-color:hsl(-120, 0%, 80%);padding:2px;}#export-svg .icon-shape rect,#export-svg .image-shape rect{opacity:0.5;background-color:hsl(-120, 0%, 80%);fill:hsl(-120, 0%, 80%);}#export-svg .node .neo-node{stroke:#000000;}#export-svg [data-look="neo"].node rect,#export-svg [data-look="neo"].cluster rect,#export-svg [data-look="neo"].node polygon{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].node rect,#export-svg [data-look="neo"].node polygon,#export-svg [data-look="neo"].node path{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].node .neo-line path{stroke:hsl(0, 0%, 70%);filter:none;}#export-svg [data-look="neo"].node circle{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].node circle .state-start{fill:#000000;}#export-svg [data-look="neo"].statediagram-cluster rect{fill:#ffffff;stroke:url(#export-svg-gradient);stroke-width:1px;}#export-svg [data-look="neo"].icon-shape .icon{fill:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].icon-shape .icon-neo path{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}</style><g><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="5" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-pointEnd"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 0 L 10 5 L 0 10 z"/></marker><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="4.5" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-pointStart"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 5 L 10 10 L 10 0 z"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="11" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-circleEnd"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="-1" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-circleStart"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="12" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="export-svg_flowchart-v2-crossEnd"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="-1" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="export-svg_flowchart-v2-crossStart"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><g class="root"><g class="clusters"/><g class="edgePaths"><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTUzLjE4NTEzMDYzNTI0NTksInkiOjU5fSx7IngiOjkyLjU0Njg3NSwieSI6OTQuNX0seyJ4Ijo5Mi41NDY4NzUsInkiOjEzMH1d" data-id="L_A_B_0" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_A_B_0" d="M153.1851306352459,59L100.20588414309853,90.01611731354028Q92.546875,94.5 92.546875,103.375L92.546875,112.25L92.546875,126"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MjQwLjI5OTI0NDM2NDc1NDEsInkiOjU5fSx7IngiOjMwMC45Mzc1LCJ5Ijo5NC41fSx7IngiOjMwMC45Mzc1LCJ5IjoxMzB9XQ==" data-id="L_A_C_1" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_A_C_1" d="M240.2992443647541,59L293.2784908569015,90.01611731354028Q300.9375,94.5 300.9375,103.375L300.9375,112.25L300.9375,126"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6OTIuNTQ2ODc1LCJ5IjoxODF9LHsieCI6OTIuNTQ2ODc1LCJ5IjoyMTYuNX0seyJ4IjoxNTMuMTg1MTMwNjM1MjQ1OSwieSI6MjUyfV0=" data-id="L_B_D_2" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_B_D_2" d="M92.546875,181L92.546875,206.4473245161372Q92.546875,216.5 101.2222027119445,221.5788752174299L122.86600281762296,234.25L149.73318285244093,249.9790951272294"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MzAwLjkzNzUsInkiOjE4MX0seyJ4IjozMDAuOTM3NSwieSI6MjE2LjV9LHsieCI6MjQwLjI5OTI0NDM2NDc1NDEsInkiOjI1Mn1d" data-id="L_C_D_3" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_C_D_3" d="M300.9375,181L300.9375,206.44732451613723Q300.9375,216.5 292.2621722880555,221.5788752174299L270.618372182377,234.25L243.75119214755907,249.9790951272294"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjMwM30seyJ4IjoxOTYuNzQyMTg3NSwieSI6MzM4LjV9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjM3NH1d" data-id="L_D_E_4" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_D_E_4" d="M196.7421875,303L196.7421875,338.5L196.7421875,356.25L196.7421875,370"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjQyNX0seyJ4IjoxOTYuNzQyMTg3NSwieSI6NDYwLjV9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjQ5Nn1d" data-id="L_E_F_5" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_E_F_5" d="M196.7421875,425L196.7421875,460.5L196.7421875,478.25L196.7421875,492"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjU0N30seyJ4IjoxOTYuNzQyMTg3NSwieSI6NTgyLjV9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjYxOH1d" data-id="L_F_G_6" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_F_G_6" d="M196.7421875,547L196.7421875,582.5L196.7421875,600.25L196.7421875,614"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjY2OX0seyJ4IjoxOTYuNzQyMTg3NSwieSI6NzA0LjV9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjc0MH1d" data-id="L_G_H_7" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_G_H_7" d="M196.7421875,669L196.7421875,704.5L196.7421875,722.25L196.7421875,736"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjc5MX0seyJ4IjoxOTYuNzQyMTg3NSwieSI6ODI2LjV9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjg2Mn1d" data-id="L_H_I_8" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_H_I_8" d="M196.7421875,791L196.7421875,826.5L196.7421875,844.25L196.7421875,858"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjkxM30seyJ4IjoxOTYuNzQyMTg3NSwieSI6OTQ4LjV9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjk4NH1d" data-id="L_I_J_9" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_I_J_9" d="M196.7421875,913L196.7421875,948.5L196.7421875,966.25L196.7421875,980"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjEwMzV9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjEwNzAuNX0seyJ4IjoxOTYuNzQyMTg3NSwieSI6MTEwNn1d" data-id="L_J_K_10" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_J_K_10" d="M196.7421875,1035L196.7421875,1070.5L196.7421875,1088.25L196.7421875,1102"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjExNTd9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjExOTIuNX0seyJ4IjoxOTYuNzQyMTg3NSwieSI6MTIyOH1d" data-id="L_K_L_11" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_K_L_11" d="M196.7421875,1157L196.7421875,1192.5L196.7421875,1210.25L196.7421875,1224"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTk2Ljc0MjE4NzUsInkiOjEyNzl9LHsieCI6MTk2Ljc0MjE4NzUsInkiOjEzMTQuNX0seyJ4IjoyNjEuMzg4Mjg3NjUzNjg4NSwieSI6MTM1MH1d" data-id="L_L_M_12" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_L_M_12" d="M196.7421875,1279L196.7421875,1304.6815116250878Q196.7421875,1314.5 205.3484131614032,1319.226054785261L229.06523757684425,1332.25L257.8821570426289,1348.0746303892004"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6NDE4LjkwNjI1LCJ5IjoxMDM1fSx7IngiOjQxOC45MDYyNSwieSI6MTA3MC41fSx7IngiOjQxOC45MDYyNSwieSI6MTEwNn1d" data-id="L_N_O_13" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_N_O_13" d="M418.90625,1035L418.90625,1070.5L418.90625,1088.25L418.90625,1102"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6NDE4LjkwNjI1LCJ5IjoxMTU3fSx7IngiOjQxOC45MDYyNSwieSI6MTE5Mi41fSx7IngiOjQxOC45MDYyNSwieSI6MTIyOH1d" data-id="L_O_P_14" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_O_P_14" d="M418.90625,1157L418.90625,1192.5L418.90625,1210.25L418.90625,1224"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6NDE4LjkwNjI1LCJ5IjoxMjc5fSx7IngiOjQxOC45MDYyNSwieSI6MTMxNC41fSx7IngiOjM1NC4yNjAxNDk4NDYzMTE1LCJ5IjoxMzUwfV0=" data-id="L_P_M_15" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_P_M_15" d="M418.90625,1279L418.90625,1304.6815116250878Q418.90625,1314.5 410.3000243385968,1319.226054785261L386.58319992315575,1332.25L357.7662804573711,1348.0746303892004"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6NjgzLjI0MjE4NzUsInkiOjQ4Ljc3MDUwMTY2Mjc3NTA3fSx7IngiOjUxNy42OTUzMTI1LCJ5Ijo5NC41fSx7IngiOjUxNy42OTUzMTI1LCJ5IjoxMzB9XQ==" data-id="L_Q_R_16" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_Q_R_16" d="M683.2421875,48.77050166277507L525.6522628447284,92.30202829223664Q517.6953125,94.5 517.6953125,102.75494630004347L517.6953125,112.25L517.6953125,126"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6NzM4LjUyMzQzNzUsInkiOjU5fSx7IngiOjczOC41MjM0Mzc1LCJ5Ijo5NC41fSx7IngiOjczOC41MjM0Mzc1LCJ5IjoxMzB9XQ==" data-id="L_Q_S_17" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_Q_S_17" d="M738.5234375,59L738.5234375,94.5L738.5234375,112.25L738.5234375,126"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6NzkzLjgwNDY4NzUsInkiOjQ5Ljg1MTA4NzIwMzU3NjAzfSx7IngiOjk0NC43NTc4MTI1LCJ5Ijo5NC41fSx7IngiOjk0NC43NTc4MTI1LCJ5IjoxMzB9XQ==" data-id="L_Q_T_18" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_Q_T_18" d="M793.8046875,49.85108720357603L936.7464669619344,92.13040435028351Q944.7578125,94.5 944.7578125,102.85443839365867L944.7578125,112.25L944.7578125,126"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6OTQ0Ljc1NzgxMjUsInkiOjE4MX0seyJ4Ijo5NDQuNzU3ODEyNSwieSI6MjE2LjV9LHsieCI6OTQ0Ljc1NzgxMjUsInkiOjI1Mn1d" data-id="L_T_U_19" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_T_U_19" d="M944.7578125,181L944.7578125,216.5L944.7578125,234.25L944.7578125,248"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTEyMC4yODEyNSwieSI6NTl9LHsieCI6MTEyMC4yODEyNSwieSI6OTQuNX0seyJ4IjoxMTIwLjI4MTI1LCJ5IjoxMzB9XQ==" data-id="L_V_W_20" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_V_W_20" d="M1120.28125,59L1120.28125,94.5L1120.28125,112.25L1120.28125,126"/></g><g class="edgeLabels"><g transform="translate(92.546875, 94.5)" class="edgeLabel"><g transform="translate(-18.4765625, -10.5)" data-id="L_A_B_0" class="label"><foreignObject height="21" width="36.953125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git init</p></span></div></foreignObject></g></g><g transform="translate(300.9375, 94.5)" class="edgeLabel"><g transform="translate(-64.5390625, -10.5)" data-id="L_A_C_1" class="label"><foreignObject height="21" width="129.078125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git clone repository-url</p></span></div></foreignObject></g></g><g transform="translate(92.546875, 216.5)" class="edgeLabel"><g transform="translate(-84.546875, -10.5)" data-id="L_B_D_2" class="label"><foreignObject height="21" width="169.09375"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git checkout -b feature-branch</p></span></div></foreignObject></g></g><g transform="translate(300.9375, 216.5)" class="edgeLabel"><g transform="translate(-84.546875, -10.5)" data-id="L_C_D_3" class="label"><foreignObject height="21" width="169.09375"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git checkout -b feature-branch</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 338.5)" class="edgeLabel"><g transform="translate(-80.109375, -10.5)" data-id="L_D_E_4" class="label"><foreignObject height="21" width="160.21875"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel">Unsupported markdown: list</span></div></foreignObject></g></g><g transform="translate(196.7421875, 460.5)" class="edgeLabel"><g transform="translate(-50.15625, -10.5)" data-id="L_E_F_5" class="label"><foreignObject height="21" width="100.3125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git checkout main</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 582.5)" class="edgeLabel"><g transform="translate(-54.25, -10.5)" data-id="L_F_G_6" class="label"><foreignObject height="21" width="108.5"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git pull origin main</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 704.5)" class="edgeLabel"><g transform="translate(-76.9609375, -10.5)" data-id="L_G_H_7" class="label"><foreignObject height="21" width="153.921875"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git checkout feature-branch</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 826.5)" class="edgeLabel"><g transform="translate(-42.25, -10.5)" data-id="L_H_I_8" class="label"><foreignObject height="21" width="84.5"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git merge main</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 948.5)" class="edgeLabel"><g transform="translate(-83.390625, -10.5)" data-id="L_I_J_9" class="label"><foreignObject height="21" width="166.78125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git push origin feature-branch</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 1070.5)" class="edgeLabel"><g transform="translate(-55.6015625, -10.5)" data-id="L_J_K_10" class="label"><foreignObject height="21" width="111.203125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Create Pull Request</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 1192.5)" class="edgeLabel"><g transform="translate(-54.4375, -10.5)" data-id="L_K_L_11" class="label"><foreignObject height="21" width="108.875"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Review &amp; Approve</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 1314.5)" class="edgeLabel"><g transform="translate(-80.109375, -10.5)" data-id="L_L_M_12" class="label"><foreignObject height="21" width="160.21875"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel">Unsupported markdown: list</span></div></foreignObject></g></g><g transform="translate(418.90625, 1070.5)" class="edgeLabel"><g transform="translate(-80.109375, -10.5)" data-id="L_N_O_13" class="label"><foreignObject height="21" width="160.21875"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel">Unsupported markdown: list</span></div></foreignObject></g></g><g transform="translate(418.90625, 1192.5)" class="edgeLabel"><g transform="translate(-42.0625, -10.5)" data-id="L_O_P_14" class="label"><foreignObject height="21" width="84.125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Emergency PR</p></span></div></foreignObject></g></g><g transform="translate(418.90625, 1314.5)" class="edgeLabel"><g transform="translate(-80.109375, -10.5)" data-id="L_P_M_15" class="label"><foreignObject height="21" width="160.21875"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel">Unsupported markdown: list</span></div></foreignObject></g></g><g transform="translate(517.6953125, 94.5)" class="edgeLabel"><g transform="translate(-67.75, -10.5)" data-id="L_Q_R_16" class="label"><foreignObject height="21" width="135.5"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git reset --soft HEAD~1</p></span></div></foreignObject></g></g><g transform="translate(738.5234375, 94.5)" class="edgeLabel"><g transform="translate(-69.6875, -10.5)" data-id="L_Q_S_17" class="label"><foreignObject height="21" width="139.375"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git reset --hard HEAD~1</p></span></div></foreignObject></g></g><g transform="translate(944.7578125, 94.5)" class="edgeLabel"><g transform="translate(-23.140625, -10.5)" data-id="L_Q_T_18" class="label"><foreignObject height="21" width="46.28125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git stash</p></span></div></foreignObject></g></g><g transform="translate(944.7578125, 216.5)" class="edgeLabel"><g transform="translate(-35.390625, -10.5)" data-id="L_T_U_19" class="label"><foreignObject height="21" width="70.78125"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>git stash pop</p></span></div></foreignObject></g></g><g transform="translate(1120.28125, 94.5)" class="edgeLabel"><g transform="translate(-80.109375, -10.5)" data-id="L_V_W_20" class="label"><foreignObject height="21" width="160.21875"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel">Unsupported markdown: list</span></div></foreignObject></g></g></g><g class="nodes"><g transform="translate(196.7421875, 33.5)" data-look="neo" data-et="node" data-node="true" data-id="A" id="flowchart-A-286" class="node default"><rect stroke="url(#gradient)" height="51" width="144.359375" y="-25.5" x="-72.1796875" data-id="A" style="" class="basic label-container"/><g transform="translate(-42.1796875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="84.359375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Local Machine</p></span></div></foreignObject></g></g><g transform="translate(92.546875, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="B" id="flowchart-B-287" class="node default"><rect stroke="url(#gradient)" height="51" width="151.390625" y="-25.5" x="-75.6953125" data-id="B" style="" class="basic label-container"/><g transform="translate(-45.6953125, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="91.390625"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>New Repository</p></span></div></foreignObject></g></g><g transform="translate(300.9375, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="C" id="flowchart-C-289" class="node default"><rect stroke="url(#gradient)" height="51" width="165.390625" y="-25.5" x="-82.6953125" data-id="C" style="" class="basic label-container"/><g transform="translate(-52.6953125, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="105.390625"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Cloned Repository</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 277.5)" data-look="neo" data-et="node" data-node="true" data-id="D" id="flowchart-D-292" class="node default"><rect stroke="url(#gradient)" height="51" width="145.921875" y="-25.5" x="-72.9609375" data-id="D" style="" class="basic label-container"/><g transform="translate(-42.9609375, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="85.921875"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Feature Branch</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 399.5)" data-look="neo" data-et="node" data-node="true" data-id="E" id="flowchart-E-294" class="node default"><rect stroke="url(#gradient)" height="51" width="143.59375" y="-25.5" x="-71.796875" data-id="E" style="" class="basic label-container"/><g transform="translate(-41.796875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="83.59375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Local Changes</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 521.5)" data-look="neo" data-et="node" data-node="true" data-id="F" id="flowchart-F-296" class="node default"><rect stroke="url(#gradient)" height="51" width="133.484375" y="-25.5" x="-66.7421875" data-id="F" style="" class="basic label-container"/><g transform="translate(-36.7421875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="73.484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Main Branch</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 643.5)" data-look="neo" data-et="node" data-node="true" data-id="G" id="flowchart-G-298" class="node default"><rect stroke="url(#gradient)" height="51" width="140.484375" y="-25.5" x="-70.2421875" data-id="G" style="" class="basic label-container"/><g transform="translate(-40.2421875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="80.484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Updated Main</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 765.5)" data-look="neo" data-et="node" data-node="true" data-id="H" id="flowchart-H-300" class="node default"><rect stroke="url(#gradient)" height="51" width="148.640625" y="-25.5" x="-74.3203125" data-id="H" style="" class="basic label-container"/><g transform="translate(-44.3203125, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="88.640625"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Back to Feature</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 887.5)" data-look="neo" data-et="node" data-node="true" data-id="I" id="flowchart-I-302" class="node default"><rect stroke="url(#gradient)" height="51" width="155" y="-25.5" x="-77.5" data-id="I" style="" class="basic label-container"/><g transform="translate(-47.5, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="95"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Merged Changes</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 1009.5)" data-look="neo" data-et="node" data-node="true" data-id="J" id="flowchart-J-304" class="node default"><rect stroke="url(#gradient)" height="51" width="192.953125" y="-25.5" x="-96.4765625" data-id="J" style="" class="basic label-container"/><g transform="translate(-66.4765625, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="132.953125"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Remote Feature Branch</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 1131.5)" data-look="neo" data-et="node" data-node="true" data-id="K" id="flowchart-K-306" class="node default"><rect stroke="url(#gradient)" height="51" width="131.171875" y="-25.5" x="-65.5859375" data-id="K" style="" class="basic label-container"/><g transform="translate(-35.5859375, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="71.171875"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Pull Request</p></span></div></foreignObject></g></g><g transform="translate(196.7421875, 1253.5)" data-look="neo" data-et="node" data-node="true" data-id="L" id="flowchart-L-308" class="node default"><rect stroke="url(#gradient)" height="51" width="149.953125" y="-25.5" x="-74.9765625" data-id="L" style="" class="basic label-container"/><g transform="translate(-44.9765625, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="89.953125"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Ready to Merge</p></span></div></foreignObject></g></g><g transform="translate(307.82421875, 1375.5)" data-look="neo" data-et="node" data-node="true" data-id="M" id="flowchart-M-310" class="node default"><rect stroke="url(#gradient)" height="51" width="140.484375" y="-25.5" x="-70.2421875" data-id="M" style="" class="basic label-container"/><g transform="translate(-40.2421875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="80.484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Main Updated</p></span></div></foreignObject></g></g><g transform="translate(418.90625, 1009.5)" data-look="neo" data-et="node" data-node="true" data-id="N" id="flowchart-N-311" class="node default"><rect stroke="url(#gradient)" height="51" width="151.375" y="-25.5" x="-75.6875" data-id="N" style="" class="basic label-container"/><g transform="translate(-45.6875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="91.375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Hotfix Required</p></span></div></foreignObject></g></g><g transform="translate(418.90625, 1131.5)" data-look="neo" data-et="node" data-node="true" data-id="O" id="flowchart-O-312" class="node default"><rect stroke="url(#gradient)" height="51" width="140.484375" y="-25.5" x="-70.2421875" data-id="O" style="" class="basic label-container"/><g transform="translate(-40.2421875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="80.484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Hotfix Branch</p></span></div></foreignObject></g></g><g transform="translate(418.90625, 1253.5)" data-look="neo" data-et="node" data-node="true" data-id="P" id="flowchart-P-314" class="node default"><rect stroke="url(#gradient)" height="51" width="140.484375" y="-25.5" x="-70.2421875" data-id="P" style="" class="basic label-container"/><g transform="translate(-40.2421875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="80.484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Quick Review</p></span></div></foreignObject></g></g><g transform="translate(738.5234375, 33.5)" data-look="neo" data-et="node" data-node="true" data-id="Q" id="flowchart-Q-317" class="node default"><rect stroke="url(#gradient)" height="51" width="110.5625" y="-25.5" x="-55.28125" data-id="Q" style="" class="basic label-container"/><g transform="translate(-25.28125, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="50.5625"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Mistakes</p></span></div></foreignObject></g></g><g transform="translate(517.6953125, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="R" id="flowchart-R-318" class="node default"><rect stroke="url(#gradient)" height="51" width="168.125" y="-25.5" x="-84.0625" data-id="R" style="" class="basic label-container"/><g transform="translate(-54.0625, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="108.125"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Undo Last Commit</p></span></div></foreignObject></g></g><g transform="translate(738.5234375, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="S" id="flowchart-S-320" class="node default"><rect stroke="url(#gradient)" height="51" width="173.53125" y="-25.5" x="-86.765625" data-id="S" style="" class="basic label-container"/><g transform="translate(-56.765625, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="113.53125"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Delete Last Commit</p></span></div></foreignObject></g></g><g transform="translate(944.7578125, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="T" id="flowchart-T-322" class="node default"><rect stroke="url(#gradient)" height="51" width="138.9375" y="-25.5" x="-69.46875" data-id="T" style="" class="basic label-container"/><g transform="translate(-39.46875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="78.9375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Save Changes</p></span></div></foreignObject></g></g><g transform="translate(944.7578125, 277.5)" data-look="neo" data-et="node" data-node="true" data-id="U" id="flowchart-U-324" class="node default"><rect stroke="url(#gradient)" height="51" width="154.484375" y="-25.5" x="-77.2421875" data-id="U" style="" class="basic label-container"/><g transform="translate(-47.2421875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="94.484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Restore Changes</p></span></div></foreignObject></g></g><g transform="translate(1120.28125, 33.5)" data-look="neo" data-et="node" data-node="true" data-id="V" id="flowchart-V-325" class="node default"><rect stroke="url(#gradient)" height="51" width="105.890625" y="-25.5" x="-52.9453125" data-id="V" style="" class="basic label-container"/><g transform="translate(-22.9453125, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="45.890625"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Conflict</p></span></div></foreignObject></g></g><g transform="translate(1120.28125, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="W" id="flowchart-W-326" class="node default"><rect stroke="url(#gradient)" height="51" width="112.109375" y="-25.5" x="-56.0546875" data-id="W" style="" class="basic label-container"/><g transform="translate(-26.0546875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="52.109375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Resolved</p></span></div></foreignObject></g></g></g></g></g><linearGradient y2="0%" x2="100%" y1="0%" x1="0%" gradientUnits="objectBoundingBox" id="export-svg-gradient"><stop stop-opacity="1" stop-color="#0042eb" offset="0%"/><stop stop-opacity="1" stop-color="#eb0042" offset="100%"/></linearGradient></svg>