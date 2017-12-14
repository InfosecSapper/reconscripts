# Reconscripts
**Reconscripts** is designed to provide a basic level of automation
for performing initial recon tasks.  
The individual stages can be requested individually, but the default is to run each script in sequence. An example of a basic workflow is as follows:  
1. Run the script with a CIDR range; this will run a ping sweep on the range and make note of the hosts which are responsive.
2. The responsive hosts will then be tested with a more in-depth **nmap** discovery
3. The subsequent **nmap** results will trigger tertiary scripts based on what services are found (e.g. **dnsenum** if UDP/53 is found open).  

The various outputs will be written to files rather than the console, which will simply provide some progress feedback to the user.

---
## Disclaimer (of sorts):
I created this while working through Offensive Security's
OSCP labs and it is in no way designed to be used commercially,
professionally, maliciously or for anything other than doing
grunt work in a lab. It's more of an exercise in Python scripting and using GitHub than it is a tool for recon. It is not designed or intended to replace or augment tools such as **sparta**, **recon-ng**, **nmap**, etc. This script was created after I spent a lot of time using the respective tools individually and manually to understand their operations, features, benefits and flaws; I simply needed a time-saving tool for a scenario in which I had limited use of existing large-scale automation tools which are more mature.  
To be clear: this was a pet project and I am treating it as disposable. However, I will support the project if there is demand and if I feel I can learn something new, so feel free to highlight issues, suggestions, etc.
