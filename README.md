# Practice DSA and upgrade your coding skills by solving these problems!
This repository contains a collection of Data Structures and Algorithms problems designed to help you enhance your coding skills. Whether you're a beginner or an experienced programmer, practicing these problems will improve your problem-solving abilities and prepare you for technical interviews.

## ⚠️ Important Disclaimer
**Please DO NOT use AI agents, ChatGPT, Copilot, or any other AI-related technology to solve these problems.** The primary goal of this repository is to develop your problem-solving and coding skills. Using AI tools to generate solutions defeats the purpose of learning and will hinder your development as a programmer. Solve these problems on your own to truly understand the concepts and improve your abilities.

## Getting Started
To get started, fork this repository on GitHub, then clone your fork to your local machine:
```bash
git clone https://github.com/your_username/dsa-training.git
```
Navigate to the project directory:
```bash
cd dsa-training
```
You can then explore the various problem categories and start solving them using your preferred programming language.

## Create a Branch for Your Solutions
To keep your contributions organized, create a new branch for your solutions. Use the following command, replacing `your_name` with your actual name (e.g., `deo-bata`):
```bash
git checkout -b your_name
# Example: git checkout -b deo-bata
```

## Create a sub-directory for your solutions
To keep your solutions organized, we provide a shell script that automatically creates the directory structure for you.

### Using the Shell Script (Recommended)
Use the provided `create-solution-structure.sh` script to automatically create the directory structure. Run it with bash:

#### Default Languages
If you don't specify any languages, the script creates directories for Python, JavaScript, C, and C++:

```bash
bash create-solution-structure.sh your_name
```

Example:
```bash
bash create-solution-structure.sh deo-bata
```

#### Custom Languages
You can specify which programming languages you want to use. Supported languages are:
- `python` - Python
- `js` - JavaScript
- `c` - C
- `cpp` - C++
- `java` - Java
- `go` - Go
- `rust` - Rust
- `dart` - Dart

To create directories for specific languages:

```bash
bash create-solution-structure.sh your_name python js
```

Example with multiple languages:
```bash
bash create-solution-structure.sh deo-bata python cpp java
```

**Note:** Make sure you're in the repository root directory when running the script. The script will validate that you enter correct language names.

This will automatically create the complete directory structure for your chosen programming languages across all problem categories (p-00 through p-05).

### Manual Directory Creation
If you prefer to create directories manually, create a sub-directory named after your GitHub username inside the `solutions/` folder and organize by language first, then by problem category:

```bash
mkdir -p solutions/your_name/python/{p-00-general,p-01-conditions,p-02-arrays,p-03-strings,p-04-loops,p-05-functions}
mkdir -p solutions/your_name/js/{p-01-conditions,p-02-arrays,p-03-strings,p-04-loops,p-05-functions}
mkdir -p solutions/your_name/c/{p-01-conditions,p-02-arrays,p-03-strings,p-04-loops,p-05-functions}
```

Your final directory structure should look like:
```
solutions/
└── deo-bata/
    ├── python/
    │   ├── p-00-general/
    │   │   └── solution-00.py
    │   ├── p-01-conditions/
    │   │   ├── solution-01.py
    │   │   └── solution-02.py
    │   ├── p-02-arrays/
    │   │   └── solution-01.py
    │   ├── p-03-strings/
    │   │   └── solution-01.py
    │   ├── p-04-loops/
    │   │   └── solution-04.py
    │   └── p-05-functions/
    │       ├── solution-01.py
    │       └── solution-05.py
    ├── js/
    │   └── p-01-conditions/
    │       └── solution-01.js
    └── c/
        └── p-01-conditions/
            └── solution-01.c
```

After creating the structure, add your solution files for each problem you solve.

You can then add your solution files inside this directory.

## Pushing Your Changes
After adding your solutions, commit and push your changes to your forked repository:
```bash
git add .
git commit -m "Add solutions for p-01-conditions by your_name"
git push origin your_name
# Example: git push origin deo-bata
```

-----------

## Contributing
We welcome contributions from the community! If you have a solution to a problem or want to add new problems, please follow these steps:
1. Fork the repository.
2. Create a new branch for your changes.
3. Add your solutions or new problems.
4. Commit your changes with a descriptive message.
5. Push your changes to your forked repository.
6. Open a pull request to the main repository.
