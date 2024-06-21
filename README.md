# DNS Switcher

DNS Switcher is a Python script with a graphical user interface (GUI) built using Tkinter. It allows users to easily switch between using Cloudflare's DNS and the default DNS settings on Windows.

## Features

- **Enable Cloudflare DNS:** Sets the DNS settings to use Cloudflare's DNS servers (1.1.1.1 and 1.0.0.1).
- **Disable Cloudflare DNS:** Resets the DNS settings back to default (DHCP).

## Installation

1. **Download the Repository:**
   ```sh
   git clone https://github.com/your-username/dns-switcher.git
   ```

2. **Install Dependencies:**
   ```sh
   pip install tk
   ```

3. **Run the Script:**
   ```sh
   python dns_switcher.py
   ```

## Usage

1. Launch the `dns_switcher.exe` file.
2. Click on the **Enable Cloudflare DNS** button to set the DNS settings to use Cloudflare's DNS servers.
3. Click on the **Disable Cloudflare DNS** button to reset the DNS settings back to default.

## Using Resource Hacker (Optional)

If you need to modify the executable file (`dns_switcher.exe`), you can use Resource Hacker to add a manifest file for administrative privileges.

1. **Download Resource Hacker:**
   - Visit the [Resource Hacker website](http://www.angusj.com/resourcehacker/).
   - Download and install Resource Hacker.

2. **Open the Executable:**
   - Launch Resource Hacker.
   - Open the `dns_switcher.exe` file using Resource Hacker.

3. **Add the Manifest Resource:**
   - In Resource Hacker, right-click on `Manifest` in the left panel.
   - Select **Add a new resource**.
   - Choose your manifest file (`dns_switcher.exe.manifest`).

4. **Save the Changes:**
   - Click on **File > Save** to save the changes to the executable file.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
