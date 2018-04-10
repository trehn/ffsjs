# ffsjs

ffsjs is a JavaScript package manager for people who are sick of JavaScript package managers. It is useful for web frontend stuff only.

## Why?

I find it annoying to have a `node_modules` directory full of crap I don't need: documentation, tests, changelogs, ...

## What does this thing do?

ffsjs will download a given package from CDNJS and put it into the current directory. That's it. CDNJS trims down their packages to just the stuff one actually needs: often just some `*.min.js` and `*.min.css`. It gets rid of all the clutter for you.

## How do I use it?

It's simple:

```
$ pip3 install ffsjs
$ ffsjs jquery
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/core.js -> jquery/core.js
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js -> jquery/jquery.js
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js -> jquery/jquery.min.js
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.map -> jquery/jquery.min.map
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.slim.js -> jquery/jquery.slim.js
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.slim.min.js -> jquery/jquery.slim.min.js
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.slim.min.map -> jquery/jquery.slim.min.map
```

## How do I pin a version?

Instead of a `package.json`, just write a small script:

```
#!/bin/sh
ffsjs jquery 1.2.3
ffsjs semantic-ui 4.5.6
ffsjs zxcvbn 7.8.9
```

## Why not just use resources from CDNJS directly?

If you can, just do that. ffsjs is meant for situations where you want to serve these files yourself for whatever reason. Maybe you want to build your site on the train without Internet access.

## Wait, this is just a download script, not a package manager!

You got me. You can uninstall packages with `rm -r`.
