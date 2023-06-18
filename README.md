# linked-in-to-json
Takes a chunk of saved jobs text copied from raw text of logged in to linked in & outputs structured JSON

## Attribution
Most or all of this was generated via ChatGPT4.
https://chat.openai.com/share/71da41db-901f-40d1-a52b-c188c7167121

## Setup
Now, you can make the Python script executable with the chmod command:

```bash
chmod +x main.py
```

Then, you can pipe data into the script like this:

```bash
echo "your job posting data" | ./main.py
```

Or from a file:

```bash
cat job_postings.txt | ./main.py
```

Just replace "your job posting data" and "```job_postings.txt```" with your actual data or file. This will output the parsed JSON to the terminal. You can then redirect this output to a file 

if you wish:

```bash
cat job_postings.txt | ./main.py > parsed_job_postings.json
```

This will save the parsed JSON to the ```parsed_job_postings.json``` file.