# mr-status-page
a self hosted status page that can be run against infa that is not yours and keeps up-to-date via cloudflare pages


# flow
1. have cron call the script
2. check the page 
    1. check per method
    2. add the data to the json
3. render the html based on the json