:loop
git pull
git pull --recurse-submodules
cd src
call gen.bat
cd ..
git add *
git commit -m "update content"
git push
timeout /t 300
goto :loop