# Tasty ModKit 🍽️

Welcome to **Tasty ModKit**, a powerful mod synchronization tool for non-Steam games. This CLI application helps you manage and update your workshop mods effortlessly, ensuring your game always runs with the latest content.

---

## Features ✨

- **Mod Folder Checking**: Verify your mod installations and ensure everything is up-to-date.
- **Modlist Upload**: Easily publish your mod list to GitHub Gists, perfect for dedicated server hosts.

---

## Table of Contents 📚

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Installation 🚀

To get started, you'll need to have Python installed on your machine. Once Python is set up, follow these steps:

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/antl3r/tasty-modkit.git
   cd tasty-modkit
   \`\`\`

2. **Install dependencies**:
   Ensure all necessary packages are installed. You can do this by running:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run the setup**:
   Before executing the main script, run the following command to set up any configurations:
   \`\`\`bash
   python setup.py install
   \`\`\`

---

## Usage 🎮

Once everything is set up, you can run the tool using the following command:

\`\`\`bash
python main.py [command] [options]
\`\`\`

### Commands

1. **Check Mod Folders**:
   To check your mod folders for updates, use:
   \`\`\`bash
   python main.py check --path /path/to/your/mods
   \`\`\`
   Replace `/path/to/your/mods` with the actual path to your mod folder.

2. **Upload Modlist to GitHub Gist**:
   To upload your current mod list, run:
   \`\`\`bash
   python main.py upload --gist-title "My Mod List" --file-path /path/to/modlist.txt
   \`\`\`
   Make sure to replace `My Mod List` with your desired Gist title and `/path/to/modlist.txt` with the path to your modlist file.

---

## Contributing 🤝

We welcome contributions! If you want to help improve Tasty ModKit, please fork the repository and submit a pull request. 

1. Fork the project.
2. Create your feature branch (\`git checkout -b feature/AmazingFeature\`).
3. Commit your changes (\`git commit -m 'Add some amazing feature'\`).
4. Push to the branch (\`git push origin feature/AmazingFeature\`).
5. Open a pull request.

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact 📫

For any inquiries, suggestions, or feedback, feel free to reach out:

- **Author**: Lovell D'Arce
- **GitHub**: [antl3r](https://github.com/antl3r)
- **Email**: your_email@example.com

---

Thank you for checking out **Tasty ModKit**! Enjoy syncing your mods! 🎉
