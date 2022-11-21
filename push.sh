git add .
read -p "[*] Type commit message:" msg
git commit -m "${msg}"
git push -u origin main || git push 
