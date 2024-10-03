# Tasty ModKit 🍫

Welcome to **Tasty ModKit**, a workshop mod synchronization tool for non-Steam games. This CLI application helps you manage and update your workshop mods effortlessly, ensuring your game always runs with matching workshop mods.

---

## Features ✨

-   **Mod Folder Checking**: Verify your mod installations and ensure everything is up-to-date.
-   **Modlist Upload**: Easily publish your mod list to GitHub Gists, perfect for dedicated server hosts.

---

## Table of Contents 📚

-   [Installation](#installation)
-   [Usage](#usage)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)
-   [OAuth](#oauth)

---

## Installation 🚀

To get started, you'll need to have Python installed on your machine. Once Python is set up, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/antl3r/tasty-modkit.git
    cd tasty-modkit
    ```

2. **Install dependencies**:
   Ensure all necessary packages are installed. You can do this by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the settings**:
   Before executing the main script, configure some important settings by opening options.cfg at ./tasty/
   If you have any trouble with OAuth, or don't know what that is, refer to [OAuth](#oauth)

---

## Usage 🎮

Once everything is set up, you can run the tool using the following command:

```bash
python main.py [command] [options]
```

### Commands

1. **Check Mod Folders**:
   To check your mod folders for updates, use:

    ```bash
    python main.py check --path /steamcmd/steamapps/workshop/content/600600/
    ```

    Replace `/steamcmd/steamapps/workshop/content/600600/` with the actual path to your mod folder.

2. **Upload Modlist to GitHub Gist**:
   To upload your current mod list, run:
    ```bash
    python main.py upload --path /steamcmd/steamapps/workshop/content/600600/
    ```
    Make sure to replace `--path /steamcmd/steamapps/workshop/content/600600/` with the path to your modlist file.

---

## Contributing 🤝

We welcome contributions! If you want to help improve Tasty ModKit, please fork the repository and submit a pull request.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact 📫

For any inquiries, suggestions, or feedback, feel free to reach out:

-   **Author**: Lovell D'Arce
-   **GitHub**: [antl3r](https://github.com/antl3r)

---

# Creating a GitHub OAuth Token 🔑

Follow these steps to create a GitHub OAuth token for accessing the GitHub API or integrating with other applications.

## Step 1: Log in to GitHub

1. Open your web browser and go to [GitHub](https://github.com).
2. Log in to your account.

## Step 2: Navigate to Developer Settings

1. In the top-right corner of the page, click on your profile picture.
2. From the dropdown menu, select **Settings**.
3. In the left sidebar, scroll down and click on **Developer settings**.

## Step 3: Create a New OAuth Token

1. Click on **Personal access tokens** in the left sidebar.
2. Click the **Tokens (classic)** tab.
3. Click the **Generate new token** button.

## Step 4: Configure Your Token

1. **Note**: You may need to authenticate again.
2. Give your token a descriptive name in the **Note** field.
3. Select the scopes or permissions you want to grant this token. For example, if you want to access repositories, check **repo**.
4. Set an expiration for your token if desired.

## Step 5: Generate and Copy the Token

1. Click the **Generate token** button at the bottom of the page.
2. **Important**: Copy your new token immediately. You won’t be able to see it again!

## Step 6: Use Your Token

You can now use your GitHub OAuth token in your applications or scripts to authenticate API requests.

---

**Note**: Treat your OAuth token like a password. Do not share it or expose it in public repositories.

This repository is dedicated to my Sabileye 🍫.
