# :honeybee: Skills Extractor Analysis

**_Open-source code for analysis built on top of Nesta's open-source [Skills Extractor Library](https://nestauk.github.io/ojd_daps_skills/build/html/about.html) and the [Open Jobs Observatory](https://github.com/nestauk/ojo_daps_mirror)_**

## :wave: Welcome!

This repo contains the source code that powers our two streamlit apps: 

1. [An app](https://github.com/nestauk/ojd-daps-skills-analysis/tree/dev/app) to demo Nesta's open-source [Skills Extractor Library](https://nestauk.github.io/ojd_daps_skills/build/html/about.html)

<p align="center">
  <img src="https://user-images.githubusercontent.com/46863334/217520975-579ebd44-e9c4-48be-ad83-96bacc16a412.gif" />
</p>

2. An [interactive blog](https://github.com/nestauk/ojd-daps-skills-analysis) to showcase regional and occupational analysis made possible with millions of job adverts and open algorithms 

<p align="center">
  <img src="https://user-images.githubusercontent.com/46863334/217522621-415750fb-493b-49c0-ab6e-00d366f85494.gif" />
</p>

## :warning: Health Warnings

Of course, with any algorithm, ours has limitations. Do investigate [our model cards](https://nestauk.github.io/ojd_daps_skills/build/html/model_card.html) to get a sense of our model evaluations, strengths and weaknesses. 

We therefore cannot guarantee the accuracy and completeness of either app.

## :floppy_disk: Setup

Create the environment
```
$ conda create --name ojd_daps_skills_analysis python=3.9
$ conda activate ojd_daps_skills_analysis
$ pip install -r requirements.txt

```

Run the analysis blog:

```
streamlit run streamlit_viz/streamlit_viz.py

```

Run the demo app:

```
streamlit run app/app/py
```
