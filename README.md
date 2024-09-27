# MailGen
</details>
MailGen is a simple Python mail generator that generates a list of random email addresses. This tool is useful for testing, development, or any scenario where you need a batch of realistic-looking email addresses.

## 🚀 Features

- ✉️ Generates a specified number of random email addresses
- 📄 Outputs the email list to a text file
- 📚 Uses diverse name data for authentic-looking email addresses

## 📊 Data Source

The name data used in MailGen is sourced from the following GitHub repository:

- **Repository**: [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)
We use the following files from this repository:

This diverse set of name data allows for the generation of a wide variety of realistic email addresses.

## 🛠️ Usage

To use MailGen, run the script with the following command:

```bash
python mailgen.py -n [NUMBER_OF_EMAILS] -o [OUTPUT_FILE]
```

For example:

```bash
python mailgen.py -n 100 -o emails.txt
```

This will generate 100 random email addresses and save them to `emails.txt`.
Running the tool with no command will output 100 random emails to `emails.txt`.

## 🔄 Automatic Updates

In this repo the email list is automatically updated **every 24h hour** using GitHub Actions. You can find the latest generated list in the `emails.txt` file in this repository.

This list contains 300 randomly created emails from the top 10 email providers. 


## 📋 Requirements

- Python 3.8+
- `requests` library
- `faker` library

To install the required libraries, run:

```bash
pip install requests faker
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

