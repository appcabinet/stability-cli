A simple script to generate AI images with Stability REST API (v2beta).

### 1. Clone Repository

Clone this repository where you hold all of your scripts. For me this is:

```~/scripts/[repo]```

### 2. Ensure Dependencies are Installed

The requirements.txt installs basic pip libraries which should be safe to use globally. Feel free to configure this as needed however.

### 3. Add .env

Create a .env file which will contain the Stability API key: `STABILITY_API_KEY=sk-...`


### 3. Create Alias

Most straightforward implementation is to create an alias, which calls the python script:

```
# .zshrc

alias stability=python3 path/to/script/main.py

```

### Done!

You are now able to execute the script!

```
stability --ratio 1:1 --seed 429000 "A cat riding a horse"
```

