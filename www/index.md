---
title: Cool-life and Temperature Display for Assurance of Cold-Chain Logistics
---

## Mission

Ideabatic had been collaborating with different project groups to develop a temperature display electronics module as an add-on product to the SMILE device. The need for such a product was identified after some users relayed that they wanted to keep track of the temperature in the SMILE device to better ensure the vaccine is stored properly.

Previous project groups have worked on different electronics housing and door slot designs, developing temperature and cool life prediction algorithms and door alert systems, and improving other mechanical features such as the self-closing mechanism and lid ergonomics. This project aims to build upon the work done by these previous groups, identifying the limitations of previous designs and improving on these features based on feedback given by SMILE's founder, Kitty Liao, and our own personal insight.


### To configure your website:

- The required files to run a basic website are included in the repository. We use here Jekyll to turn markdown files into html that will be automatically updated on the website. The component responsible for this is a GitHub action, which is specified in the folder .github/workflows. There is no need to change this file. However:

- In the settings of your repository, go the section "Pages", and select GitHub Actions in the drop down menu to indicate that this is the way you'd like the webpage to be generated.

- Each time you update the markdown files in the www folder of the repository, it will regenerate the web content. The address of the website will be:

```
https://technology-for-the-poorest-billion.github.io/[your repo name here]
```

- index.md is the root of your website. To link another page from here, located within the www folder, use the following syntax:

```
This is a [link](linkedpage.md) to interesting content.
```

Which results in:

This is a [link](linkedpage.md) to interesting content.

- Pay attention to the header of the markdown files in this section. It contains a title section that you will need to reproduce for each page to render them properly.


