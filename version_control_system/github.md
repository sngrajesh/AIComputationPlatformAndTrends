### Git oann

#### Table of Contents
1. [Initial Setup](#initial-setup)
2. [Basic Git Operations](#basic-git-operations)
3. [Branching and Merging](#branching-and-merging)
4. [Remote Operations](#remote-operations)
5. [Visual Studio Code Git Interface](#visual-studio-code-git-interface)
6. [Advanced Operations](#advanced-operations)
7. [Best Practices](#best-practices)

#### Initial Setup

##### Installing Git
1. Download Git from [git-scm.com](https://git-scm.com)
2. Install Git with recommended settings
3. Verify installation: 
```bash
git --version
```

##### First-time Git Configuration
```bash
### Set your username
git config --global user.name "Your Name"

### Set your email
git config --global user.email "your.email@example.com"

### Set default branch name
git config --global init.defaultBranch main
```

##### Setting up a New Repository
```bash
### Initialize a new repository
git init

### Clone an existing repository
git clone <repository-url>
```

#### Basic Git Operations

##### Working with Changes

###### Staging Files
- Using VSCode UI: Click the + (plus) icon next to files in the Source Control panel
- Using command line:
```bash
### Stage specific file
git add filename.ext

### Stage all changes
git add .

### Stage parts of a file
git add -p filename.ext
```

###### Committing Changes
- VSCode UI: Write commit message and press Ctrl+Enter (Cmd+Enter on Mac)
- Command line:
```bash
### Commit with message
git commit -m "Your commit message"

### Commit staged changes and skip staging area
git commit -am "Your commit message"
```

###### Viewing Status and History
```bash
### Check status of working directory
git status

### View commit history
git log

### View specific commit
git show <commit-hash>
```

#### Branching and Merging

##### Branch Operations
```bash
### Create new branch
git branch <branch-name>

### Switch to branch
git checkout <branch-name>

### Create and switch to new branch
git checkout -b <branch-name>

### List all branches
git branch -a

### Delete branch
git branch -d <branch-name>
```

##### Merging
```bash
### Merge branch into current branch
git merge <branch-name>

### Abort merge in case of conflicts
git merge --abort
```

#### Remote Operations

##### Working with Remotes
```bash
### Add remote repository
git remote add origin <repository-url>

### View remote repositories
git remote -v

### Push to remote
git push -u origin <branch-name>

### Pull from remote
git pull origin <branch-name>

### Fetch remote changes
git fetch origin
```

#### Visual Studio Code Git Interface

##### Source Control Panel Features
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

##### Useful VSCode Git Commands (Command Palette)
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

#### Advanced Operations

##### Stashing Changes
```bash
### Stash current changes
git stash

### List stashes
git stash list

### Apply most recent stash
git stash pop

### Apply specific stash
git stash apply stash@{n}
```

##### Reverting Changes
```bash
### Revert last commit
git revert HEAD

### Revert specific commit
git revert <commit-hash>

### Reset to specific commit (careful!)
git reset --hard <commit-hash>
```

##### Resolving Merge Conflicts
1. Open conflicted file in VSCode
2. Look for conflict markers (<<<<<<, =======, >>>>>>>)
3. Choose which changes to keep
4. Stage resolved files
5. Commit the merge

#### Best Practices

##### Commit Messages
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- First line should be 50 characters or less
- Add detailed description after blank line if needed

##### Branching Strategy
1. Main/Master branch: stable, production-ready code
2. Development branch: integration branch for features
3. Feature branches: individual features
4. Hotfix branches: urgent fixes for production

##### Regular Operations
1. Pull before starting new work
2. Create feature branch for new work
3. Make small, focused commits
4. Write clear commit messages
5. Pull and merge main branch regularly
6. Push changes frequently

##### Git Flow 

<svg aria-roledescription="flowchart-v2" role="graphics-document document" viewBox="0 0 368.79998779296875 677" style="max-width: 368.79998779296875px;" class="flowchart" xmlns="http://www.w3.org/2000/svg" width="100%" id="export-svg"><style xmlns="http://www.w3.org/1999/xhtml">@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"); p {margin: 0;}</style><style>#export-svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:14px;fill:#333;}#export-svg .error-icon{fill:#ffffff;}#export-svg .error-text{fill:#000000;stroke:#000000;}#export-svg .edge-thickness-normal{stroke-width:1px;}#export-svg .edge-thickness-thick{stroke-width:3.5px;}#export-svg .edge-pattern-solid{stroke-dasharray:0;}#export-svg .edge-thickness-invisible{stroke-width:0;fill:none;}#export-svg .edge-pattern-dashed{stroke-dasharray:3;}#export-svg .edge-pattern-dotted{stroke-dasharray:2;}#export-svg .marker{fill:#000000;stroke:#000000;}#export-svg .marker.cross{stroke:#000000;}#export-svg svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:14px;}#export-svg p{margin:0;}#export-svg .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#export-svg .cluster-label text{fill:#000000;}#export-svg .cluster-label span{color:#000000;}#export-svg .cluster-label span p{background-color:transparent;}#export-svg .label text,#export-svg span{fill:#333;color:#333;}#export-svg .node rect,#export-svg .node circle,#export-svg .node ellipse,#export-svg .node polygon,#export-svg .node path{fill:#ffffff;stroke:#000000;stroke-width:1px;}#export-svg .rough-node .label text,#export-svg .node .label text,#export-svg .image-shape .label,#export-svg .icon-shape .label{text-anchor:middle;}#export-svg .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#export-svg .rough-node .label,#export-svg .node .label,#export-svg .image-shape .label,#export-svg .icon-shape .label{text-align:center;}#export-svg .node.clickable{cursor:pointer;}#export-svg .root .anchor path{fill:#000000!important;stroke-width:0;stroke:#000000;}#export-svg .arrowheadPath{fill:#000000;}#export-svg .edgePath .path{stroke:#000000;stroke-width:2.0px;}#export-svg .flowchart-link{stroke:#000000;fill:none;}#export-svg .edgeLabel{background-color:hsl(-120, 0%, 80%);text-align:center;}#export-svg .edgeLabel p{background-color:hsl(-120, 0%, 80%);}#export-svg .edgeLabel rect{opacity:0.5;background-color:hsl(-120, 0%, 80%);fill:hsl(-120, 0%, 80%);}#export-svg .labelBkg{background-color:rgba(204, 204, 204, 0.5);}#export-svg .cluster rect{fill:#ffffff;stroke:hsl(0, 0%, 90%);stroke-width:1px;}#export-svg .cluster text{fill:#000000;}#export-svg .cluster span{color:#000000;}#export-svg div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:#ffffff;border:1px solid hsl(0, 0%, 90%);border-radius:2px;pointer-events:none;z-index:100;}#export-svg .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#export-svg rect.text{fill:none;stroke-width:0;}#export-svg .icon-shape,#export-svg .image-shape{background-color:hsl(-120, 0%, 80%);text-align:center;}#export-svg .icon-shape p,#export-svg .image-shape p{background-color:hsl(-120, 0%, 80%);padding:2px;}#export-svg .icon-shape rect,#export-svg .image-shape rect{opacity:0.5;background-color:hsl(-120, 0%, 80%);fill:hsl(-120, 0%, 80%);}#export-svg .node .neo-node{stroke:#000000;}#export-svg [data-look="neo"].node rect,#export-svg [data-look="neo"].cluster rect,#export-svg [data-look="neo"].node polygon{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].node rect,#export-svg [data-look="neo"].node polygon,#export-svg [data-look="neo"].node path{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].node .neo-line path{stroke:hsl(0, 0%, 70%);filter:none;}#export-svg [data-look="neo"].node circle{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].node circle .state-start{fill:#000000;}#export-svg [data-look="neo"].statediagram-cluster rect{fill:#ffffff;stroke:url(#export-svg-gradient);stroke-width:1px;}#export-svg [data-look="neo"].icon-shape .icon{fill:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg [data-look="neo"].icon-shape .icon-neo path{stroke:url(#export-svg-gradient);filter:drop-shadow( 0px 1px 2px rgba(0, 0, 0, 0.25));}#export-svg :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}</style><g><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="5" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-pointEnd"><path style="stroke-width: 1px; stroke-dasharray: 1px, 0px;" class="arrowMarkerPath" d="M 0 0 L 10 5 L 0 10 z"/></marker><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="4.5" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-pointStart"><path style="stroke-width: 1px; stroke-dasharray: 1px, 0px;" class="arrowMarkerPath" d="M 0 5 L 10 10 L 10 0 z"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="11" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-circleEnd"><circle style="stroke-width: 1px; stroke-dasharray: 1px, 0px;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="-1" viewBox="0 0 10 10" class="marker flowchart-v2" id="export-svg_flowchart-v2-circleStart"><circle style="stroke-width: 1px; stroke-dasharray: 1px, 0px;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="12" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="export-svg_flowchart-v2-crossEnd"><path style="stroke-width: 2px; stroke-dasharray: 1px, 0px;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="-1" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="export-svg_flowchart-v2-crossStart"><path style="stroke-width: 2px; stroke-dasharray: 1px, 0px;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><g class="root"><g class="clusters"/><g class="edgePaths"><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MTQ0LjQ5ODc2NTY2NDAyMjQ3LCJ5Ijo1OX0seyJ4Ijo4OC45NDk5OTY5NDgyNDIxOSwieSI6OTQuNX0seyJ4Ijo4OC45NDk5OTY5NDgyNDIxOSwieSI6MTMwfV0=" data-id="L_A_B_0" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_A_B_0" d="M144.49876566402247,59L96.42828431013295,89.72079053263147Q88.94999694824219,94.5 88.94999694824219,103.375L88.94999694824219,112.25L88.94999694824219,126"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjE4MX0seyJ4Ijo4OC45NDk5OTY5NDgyNDIxOSwieSI6MjE2LjV9LHsieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjI1Mn1d" data-id="L_B_C_1" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_B_C_1" d="M88.94999694824219,181L88.94999694824219,216.5L88.94999694824219,234.25L88.94999694824219,248"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjMwM30seyJ4Ijo4OC45NDk5OTY5NDgyNDIxOSwieSI6MzM4LjV9LHsieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjM3NH1d" data-id="L_C_D_2" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_C_D_2" d="M88.94999694824219,303L88.94999694824219,338.5L88.94999694824219,356.25L88.94999694824219,370"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjQyNX0seyJ4Ijo4OC45NDk5OTY5NDgyNDIxOSwieSI6NDYwLjV9LHsieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjQ5Nn1d" data-id="L_D_E_3" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_D_E_3" d="M88.94999694824219,425L88.94999694824219,460.5L88.94999694824219,478.25L88.94999694824219,492"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjU0N30seyJ4Ijo4OC45NDk5OTY5NDgyNDIxOSwieSI6NTgyLjV9LHsieCI6ODguOTQ5OTk2OTQ4MjQyMTksInkiOjYxOH1d" data-id="L_E_F_4" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_E_F_4" d="M88.94999694824219,547L88.94999694824219,582.5L88.94999694824219,600.25L88.94999694824219,614"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6MjI0LjMwMTIyMjEyODk0NjI4LCJ5Ijo1OX0seyJ4IjoyNzkuODQ5OTkwODQ0NzI2NTYsInkiOjk0LjV9LHsieCI6Mjc5Ljg0OTk5MDg0NDcyNjU2LCJ5IjoxMzB9XQ==" data-id="L_A_G_5" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_A_G_5" d="M224.30122212894628,59L272.3717034828358,89.72079053263147Q279.84999084472656,94.5 279.84999084472656,103.375L279.84999084472656,112.25L279.84999084472656,126"/><path marker-end="url(#export-svg_flowchart-v2-pointEnd)" data-points="W3sieCI6Mjc5Ljg0OTk5MDg0NDcyNjU2LCJ5IjoxODF9LHsieCI6Mjc5Ljg0OTk5MDg0NDcyNjU2LCJ5IjoyMTYuNX0seyJ4IjoyNzkuODQ5OTkwODQ0NzI2NTYsInkiOjI1Mn1d" data-id="L_G_H_6" data-et="edge" data-edge="true" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_G_H_6" d="M279.84999084472656,181L279.84999084472656,216.5L279.84999084472656,234.25L279.84999084472656,248"/></g><g class="edgeLabels"><g transform="translate(88.94999694824219, 94.5)" class="edgeLabel"><g transform="translate(-68.07499694824219, -10.5)" data-id="L_A_B_0" class="label"><foreignObject height="21" width="136.14999389648438"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Create feature branch</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 216.5)" class="edgeLabel"><g transform="translate(-41.241668701171875, -10.5)" data-id="L_B_C_1" class="label"><foreignObject height="21" width="82.48333740234375"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Development</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 338.5)" class="edgeLabel"><g transform="translate(-41.241668701171875, -10.5)" data-id="L_C_D_2" class="label"><foreignObject height="21" width="82.48333740234375"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Development</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 460.5)" class="edgeLabel"><g transform="translate(-39.68333435058594, -10.5)" data-id="L_D_E_3" class="label"><foreignObject height="21" width="79.36666870117188"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Pull Request</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 582.5)" class="edgeLabel"><g transform="translate(-29.958335876464844, -10.5)" data-id="L_E_F_4" class="label"><foreignObject height="21" width="59.91667175292969"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Approved</p></span></div></foreignObject></g></g><g transform="translate(279.84999084472656, 94.5)" class="edgeLabel"><g transform="translate(-43.18333435058594, -10.5)" data-id="L_A_G_5" class="label"><foreignObject height="21" width="86.36666870117188"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Hotfix needed</p></span></div></foreignObject></g></g><g transform="translate(279.84999084472656, 216.5)" class="edgeLabel"><g transform="translate(-9.333335876464844, -10.5)" data-id="L_G_H_6" class="label"><foreignObject height="21" width="18.666671752929688"><div class="labelBkg" xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="edgeLabel"><p>Fix</p></span></div></foreignObject></g></g></g><g class="nodes"><g transform="translate(184.39999389648438, 33.5)" data-look="neo" data-et="node" data-node="true" data-id="A" id="flowchart-A-170" class="node default"><rect stroke="url(#gradient)" height="51" width="102.78334045410156" y="-25.5" x="-51.39167022705078" data-id="A" style="" class="basic label-container"/><g transform="translate(-21.39167022705078, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="42.78334045410156"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Master</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="B" id="flowchart-B-171" class="node default"><rect stroke="url(#gradient)" height="51" width="108.23333740234375" y="-25.5" x="-54.116668701171875" data-id="B" style="" class="basic label-container"/><g transform="translate(-24.116668701171875, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="48.23333740234375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Feature</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 277.5)" data-look="neo" data-et="node" data-node="true" data-id="C" id="flowchart-C-173" class="node default"><rect stroke="url(#gradient)" height="51" width="119.89999389648438" y="-25.5" x="-59.94999694824219" data-id="C" style="" class="basic label-container"/><g transform="translate(-29.949996948242188, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="59.899993896484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Commit 1</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 399.5)" data-look="neo" data-et="node" data-node="true" data-id="D" id="flowchart-D-175" class="node default"><rect stroke="url(#gradient)" height="51" width="119.89999389648438" y="-25.5" x="-59.94999694824219" data-id="D" style="" class="basic label-container"/><g transform="translate(-29.949996948242188, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="59.899993896484375"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Commit 2</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 521.5)" data-look="neo" data-et="node" data-node="true" data-id="E" id="flowchart-E-177" class="node default"><rect stroke="url(#gradient)" height="51" width="143.26666259765625" y="-25.5" x="-71.63333129882812" data-id="E" style="" class="basic label-container"/><g transform="translate(-41.633331298828125, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="83.26666259765625"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Code Review</p></span></div></foreignObject></g></g><g transform="translate(88.94999694824219, 643.5)" data-look="neo" data-et="node" data-node="true" data-id="F" id="flowchart-F-179" class="node default"><rect stroke="url(#gradient)" height="51" width="161.89999389648438" y="-25.5" x="-80.94999694824219" data-id="F" style="" class="basic label-container"/><g transform="translate(-50.94999694824219, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="101.89999389648438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Merge to Master</p></span></div></foreignObject></g></g><g transform="translate(279.84999084472656, 155.5)" data-look="neo" data-et="node" data-node="true" data-id="G" id="flowchart-G-181" class="node default"><rect stroke="url(#gradient)" height="51" width="144.01666259765625" y="-25.5" x="-72.00833129882812" data-id="G" style="" class="basic label-container"/><g transform="translate(-42.008331298828125, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="84.01666259765625"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Hotfix Branch</p></span></div></foreignObject></g></g><g transform="translate(279.84999084472656, 277.5)" data-look="neo" data-et="node" data-node="true" data-id="H" id="flowchart-H-183" class="node default"><rect stroke="url(#gradient)" height="51" width="161.89999389648438" y="-25.5" x="-80.94999694824219" data-id="H" style="" class="basic label-container"/><g transform="translate(-50.94999694824219, -10.5)" style="" class="label"><rect/><foreignObject height="21" width="101.89999389648438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: normal; line-height: 1.5; max-width: 200px; text-align: center;"><span class="nodeLabel"><p>Merge to Master</p></span></div></foreignObject></g></g></g></g></g><linearGradient y2="0%" x2="100%" y1="0%" x1="0%" gradientUnits="objectBoundingBox" id="export-svg-gradient"><stop stop-opacity="1" stop-color="#0042eb" offset="0%"/><stop stop-opacity="1" stop-color="#eb0042" offset="100%"/></linearGradient></svg>

##### Troubleshooting Common Issues
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