# sowatt-websec-framework
My framework and checklist for recon, enumeration, and testing web application security.

1. Getting started
- [ ] Get in the right state of mind! VDP programs should be fun!
- [ ] Read the VDP guidelines fully.  
- [ ] Use the TemplateGen.py Script to create a note taking template for the program. Fill in necessary info.

2. Recon
- [ ] Using the asset list from the template, start by manually walking through applications. Take notes on behaviors, endpoints, anything that seems important.
- [ ] Use Sublist3r to discover subdomains and make sure they are in scope. Add these to notes.
- [ ] Search any endpoints for "Index of /" using google. 
- [ ] Check DNS records, look for floating or outdated records that can be potientially taken over. dig, dig, dig.
- [ ] Were you given an IP with a CIDR block? I usually build out a list of all the IP's contained in that block. (note to self to script this away or find someone else who has) 
- [ ] Use who.is to check for more info.
- [ ] Look if there are any low hanging fruit info disclosure issues (public tokens that shouldn't be, stack traces, etc). Make a courtsey report, expect nothing :)
- [ ] Keep organized tracked of all this info in the template.

3. Enumeration
- [ ] I usually dig a little deeper into the artifacts that were found in the recon portion. 
- [ ] Got a CIDR block? start running some non-intrusive scans (MAKE SURE THE GUIDELINES OKAY THIS).
- [ ] Can you find any services running? What type of Database? What type of Cache? What's the web server version? Is it containerized?
- [ ] It's around here where I start using Burp Suite to manually walk through requests. I typically start with login flow and account creation just to see how those function. Look for how JJWT tokens are set and used if they are. 
- [ ] Perform some requests unauthenticated, authenticated, with super user (if applicable). Note the differences and see if one of these can do something that it shouldn't. 
- [ ] Are any services and their current versions found on exploit-db? 
- [ ] Are there any fields for a user to input anything? Test these like crazy, use escape characters, try to bypass filters, anything + everything.
- [ ] Explore! It's a big scavenger hunt for anything and everything (in scope).

4. Find a vulnerability, test the vulnerability, test it again, write a report.
- [ ] Congrats on the finding! Make sure to test with a variety of browsers, enviornments, etc. You really want to give a good idea to the report reader of what is required to create a POC.
- [ ] Using the info found [At this link](https://docs.hackerone.com/en/articles/8496338-report-templates), you can use a variety of templates for reporting. Following these are the way to go when creating a report
- [ ] Submit the report when you are sure you have all the relevant information and understand that the report reader probably has a lot on their plate. The amount of turbo cringe reporter attitudes I've seen makes me sad, don't be like those reporters!
- [ ] Have fun! Don't do this for something stupid like cloth papers with dead peoples faces on it, do it for something cool like learning, the opportunity to help, and the challenge!

Thanks for using this non comprehensive list. There are other great resources that exist when it comes to web security testing, here are others that I like to refer to!:
[OWASP Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/stable/)
