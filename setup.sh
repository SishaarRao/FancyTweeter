#!/bin/bash
heroku create
git init
git add --all
git commit -m "Initial Commit"
git push heroku master
heroku ps:scale worker=1
echo "Setup complete. Run 'heroku ps' after some time. If you see 'worker: crashed' refer to README. Otherwise, FancyTweeter is up!"
