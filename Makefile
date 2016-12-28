all: 2015.csv 2014.csv 2016.csv
.PHONY: clean

2016.csv:
	@./app.py 2016 > 2016.csv

2015.csv:
	@./app.py 2015 > 2015.csv

2014.csv:
	@./app.py 2014 > 2014.csv

clean:
	$(RM) -f 2014.csv 2015.csv
