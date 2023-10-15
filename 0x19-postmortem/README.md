# 0x19. POSTMORTEM



Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

- To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
- And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

Here is a sample Postmortem/Incident report:



## **Incident Report: Operation CatTimeAPI - The Feline Downtime Fiasco**

![CatTimeAPI](https://cdn-images-1.medium.com/max/800/1*scRGA2VHjNp6pGqPnbRkZQ.jpeg)

### **The Feline Fun-Pocalypse:**

- **Duration:** From 09:00 AM to 11:30 AM (UTC), October 12, 20XX.
- **Impact:** The CatTimeAPI web service, your go-to source for feline-related fun, experienced a significant outage, leaving cat lovers in a state of purr-plexity. 25% of our users were affected, encountering slow page load times and intermittent unavailability.
- **Root Cause:** It turns out, our sudden surge in cat-loving fans due to a viral "Kitty Karaoke" campaign combined with a cat-astrophic load balancer issue created this fur-midable outage.

### **Timeline - The Tale of the Tail:**

- **09:00 AM:** Our trusty automated monitoring systems detected the fur-mageddon.
- **09:05 AM:** The operations team leaped into action - but no amount of cat-like reflexes could've prepared them for this.

![Cat Time](C:\Users\micha\Downloads\gilly-z0Gj9gr92A8-unsplash.jpg)

**09:10 AM:** Initial investigation revealed a suspicious spike in incoming traffic - were the cats staging a coup?

- **09:30 AM:** Misleading path: We thought it was a DDoS attack, but it turned out the cat video craze was very real.
- **09:45 AM:** The development team got involved, convinced the cats must've hacked our servers.
- **10:15 AM:** The mystery unraveled - our load balancer was misconfigured, distributing traffic like a cat chasing a laser pointer.
- **10:30 AM:** Our networking team was brought in - yes, cat videos require serious network handling!
- **11:30 AM:** The issue was resolved; the CatTimeAPI was back to normal operation, but with 100% more cat memes.

### **Root Cause and Resolution - A Tail of Two Kitties:**

- **Root Cause:** The sudden influx of cat lovers from the viral campaign exposed a misconfigured load balancer. This caused some backend servers to be over-pawed, leading to high latency and service disruptions.

- **Resolution:** We performed a purr-fect update to the load balancer's configuration, ensuring traffic was distributed evenly across backend servers. Additional resources were added to handle the increased cat-erly load.

### **Corrective and Preventative Measures - Lessons from the Litter Box:**

1. **Load Balancer Configuration Review:** We'll perform regular audits of load balancer configurations, making sure they are as agile as a cat mid-pounce.

2. **Capacity Planning:** Better capacity planning to handle the cat-tastrophic traffic spikes that accompany viral cat videos.

3. **Monitoring Enhancements:** Improved monitoring to detect and alert on traffic spikes, ensuring we're not caught cat-napping.

![Watchful Cat](https://unsplash.com/photos/a-cat-sitting-in-the-window-of-a-red-building-aFLgWQiOkGg)

4. **DDoS Mitigation Plan:** Developing a plan to handle potential DDoS attacks and ensuring we don't chase our tails unnecessarily.

5. **Team Training:** We'll train our teams to recognize and respond to load balancer misconfigurations and other feline-esque issues. Cat-astrophes beware!

### **Pawsitively Conclusion:**

CatTimeAPI is back on its feet, or rather, on its paws. Our cat-loving users are happily scrolling through cat memes once more, and we're better prepared to handle the next cat-tastrophy. Stay tuned for more purr-fectly smooth cat time experiences!

![Happy Cat](https://unsplash.com/photos/uy5t-CJuIK4)

*This incident report was brought to you by CatTimeAPI - where downtime is strictly reserved for catnaps!*
