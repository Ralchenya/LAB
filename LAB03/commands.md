2. tree -L 2
3. cd /etc/
4. ls -a /etc
5. cd
6. mkdir structure
7. mkdir 2018 - mkdir 2023
cd 2018
mkdir files
mkdir pictures
mkdir .passwords
V 2019-2023 analogichno
8. cd structure
cd 2018
cd files
touch data.md 
V 2019-2023 analogichno
9. cd structure
cd 2018
cd pictures
touch picture.png
V 2019-2023 analogichno
10. cd structure
cd 2018
cd .passwords
touch passwords.txt
V 2019-2023 analogichno
11. touch -md 20240101 structure/{2018..2023}/files/data.md
12. cd structure
cd 2018
cd .passwords
touch -mat 201806100000.00 .passwords.txt 
V 2019-2023 analogichno
13. cp -r ~/structure/2023 ~/Downloads/2025 
14. touch -mat 202506100000.00 .passwords.txt 
15. cp -rp ~/Downloads/2025 ~/structure/
16. mv ~/structure/2025 ~/structure/2024
17. mv home/ekaterina/structure/2024/pictures/picture.png home/ekaterina/structure/2024/pictures/image.png
18. mv home/ekaterina/structure/2024/ ~/Documents
 mv home/ekaterina/structure/2018/ ~/Documents
19. rmdir ~/Documents/2024 (Directory not empty)
20. rm -r ~/Documents/2024
21. cat > ~/structure/2019/files/data.md
22. nano ~/structure/2020/files/data.md (ctrl+o enter ctrl+x)
23. code ~/structure/2021/files/data.md 
24. cat ~/structure/2020/files/data.md > ~/structure/2022/files/data.md
25. cd structure
mkdir soft_links
mkdir hard_links
26. ln -s ~/structure/2019 ~/stricture/soft_links/2019
V 2020-2023 analogichno
27. ln ~/structure/2020/files/data.md ~/structure/hard_links/data.md
ln ~/structure/2021/.passwords/.passwords.txt ~/stricture/hard_links/.passwords.txt
28. mkdir archives
29. 
30. mv ~/Downloads/image.jpg ~/structure/archives
31. tar -cf ~/structure/archives/image.tar -C ~/structure/archives image.jpg
tar -czf ~/structure/archives/image.tar.gz -C ~/structure/archives image.jpg
tar -cjf ~/structure/archives/image.tar.bz2 -C ~/structure/archives image.jpg
32. zip -rP 1111 ~/structure/structure.zip ~/structure
