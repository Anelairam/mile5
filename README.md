#ImageLand
---

## Overview
---

<details><summary>Contents</summary>
<p>

* [User Experience](#User-Experience)
  * [Strategy Plane](#Strategy-Plane)
  * [Scope Plane](#Scope-Plane)
    * [User Storie](#User-Stories)
  * [Skeleton Plane](#Skeleton-Plane)
  * [Wireframes](#Wireframes)
    * [Full Screen](#Full-Screen)
    * [Mobile](#mobile)
  * [Design](#design)
    * [Images](#images)
    * [Colours](#colours)
* [Database View](#database-view)
* [Data Models](#data-models)
* [Technologies Used](#technologies-used)
* [Testing](#testing-validation)
* [Deployment](#deployment)
* [Credits](#credits)

</p>
</details>

## User Experience
---

### Strategy Plane
---

### Scoop Plane
---

#### User Stories
---

### Skeleton Plane
---

### Wireframes
---

#### Full Screen

* Main Page
![image](https://user-images.githubusercontent.com/25570623/176245314-e94efa3d-7be8-44a1-a242-e1f62df93123.png)
* Products Page
![image](https://user-images.githubusercontent.com/25570623/176246335-a9bad98f-1171-4f8d-8ccf-e508dda5c02a.png)
* Product Details Page
![image](https://user-images.githubusercontent.com/25570623/176247468-fe839dea-3b45-4d08-b109-0df352380b8f.png)
* Shopping bag
![image](https://user-images.githubusercontent.com/25570623/176247934-d5559e97-db38-4d4d-ab0d-23e5312dc82a.png)

#### Mobile

* Main Page
![image](https://user-images.githubusercontent.com/25570623/176249485-e7310264-950e-48a9-b1bd-c86c9d065f79.png)
* Product Page
![image](https://user-images.githubusercontent.com/25570623/176249812-b91bbedc-8a57-4f3e-9718-2fd09c598d5f.png)
* Product Detail Page
![image](https://user-images.githubusercontent.com/25570623/176251656-61cd90f7-e278-4669-af0f-eb0ed2cb3318.png)
* Shopping Bag
![image](https://user-images.githubusercontent.com/25570623/176252752-ba9ffad7-dd29-40c4-8a19-ed6c25220edc.png)

### Design
---

#### Images
---

#### Colours
---

### Database View
---

### Data Models
---

### Technologies Used
---

### Testing & Validation
---

### Deployment
---

### Credits
---



## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
