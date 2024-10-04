from finder import AdFinder

# Example usage
url = "https://divar.ir/s/ahvaz/car?color=%D8%B3%D9%81%DB%8C%D8%AF&chassis_status=both-healthy&gearbox=manual&motor_status=healthy&sort=sort_date&q=%DA%A9%D9%88%DB%8C%DB%8C%DA%A9%20r"
finder = AdFinder(url)
finder.set_crawling_time(2)  # Set the crawling time to * minute
ads = finder.run()  # Start the crawler