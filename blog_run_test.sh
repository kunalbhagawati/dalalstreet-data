while true; do 
	inotifywait dalalstreet_data/ tests/ -q -e create -e close_write -e attrib -e move 
	clear
	env/bin/python3 -m unittest tests.test_util
done
```
