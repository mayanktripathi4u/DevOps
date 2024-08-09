# Google Cloud Monitoring with Self-hosted Grafana

## Steps
* Setup Grafana on Google Cloud VM Instance
* Configure Authentication
* Configure Google Cloud Monitoring in Grafana
* Configure Google Cloud Logging in Grafana
* Play around Grafana Features

# What is Grafana?
* Grafana is an open-source platform for visualizing and analyzing your data.
* It allows you to create interactive dashboards that display metrics, logs, and traces from various sources.

# Setup
1. Open GCP Console
2. Create VM Instance to host Grafana.
   1. Name: grafana-server
   2. Associate Custom Service Account
   3. Default rest of the fields
   4. Debian Image
   5. Firewall --> Allow HTTP and HTTPS
   6. Install the Ops Agent for monitoring.
   7. Create
3. Create a Custom Service Account with no roles as of now.
4. SSH into the VM Instance. If not able to SSH then create a firewall to allow port 22.
5. RUn the following commands to install Grafana. Refer official doc 
   https://grafana.com/grafana/download?edition=oss 
   or
   https://grafana.com/grafana/download/10.4.2?edition=oss 
   ```
    sudo apt-get update
    sudo apt-get install -y adduser libfontconfig1 musl
    wget https://dl.grafana.com/oss/release/grafana_10.4.2_amd64.deb
    sudo dpkg -i grafana_10.4.2_amd64.deb
    ```
6. Once download and Install is complete, terminal itself will provide the command to start the Grafana.
   ```
   sudo systemctl start grafana-server
   ```
7. Check the Status of Grafana
   ```
   sudo systemctl status grafana-server
   ```
8. Check for the port on which Grafana is running. Usually it is 3000 port. Also get the admin user name and passcode to use later in the following steps.
   ```
   sudo cd /etc/grafana/
   ls 
   sudo grep http_port grafana.ini

   sudo grep -i5 admin_user grafana.ini
   ```
9. Once the port is identified get the public IP of VM instance, and open that IP into browser from local workstation with port 3000. Example: 34.86.240.95:3000 This will open the login page. Use the admin user name passcode to login. It will open a Home / Welcome Page, and in Dashboard it will be empty as yet we did not created any Dashboards.
10. Add a Data Source to Grafana, for this click on "Connections", and GCP has provided inbuild plugin, will use that. 
11. 
12. 
13. 
