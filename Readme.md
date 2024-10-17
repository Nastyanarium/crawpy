# Web Crawler

This project is a web crawler built in Python that extracts data from web pages based on specified tasks and extractors. The crawler supports templates for dynamic URL generation and can handle both JSON and YAML task definitions.

## Features

- Crawl web pages using specified URLs and extractors.
- Supports dynamic URL templates with replacement placeholders.
- Extracts data based on specified CSS selectors and attributes.
- Outputs extracted data in JSON format.
- Reads task definitions from both JSON and YAML files.

## Requirements

- Python 3.x

You can install the required packages using:

```bash
pip install requests lxml.html httpx PyYAML
```



## Usage
To run the crawler, use the following command:

```bash
python3 main.py <task_file>
```

- <task_file>: Path to the JSON or YAML file containing flow. 

Example
```bash
python main.py flow.yml
```


# Tasks and flow example:

```yaml
name: github issues
url: https://github.com/microsoft/vscode/issues?page=1
extractors:
  - name: issues
    selector: .Box-row
    attributes:
      - name: id
        attribute: id
      - name: title
        selector: .Link--primary
      - name: url
        selector: .Link--primary
        attribute: href
      - name: tag
        selector: .IssueLabel
        attribute: data-name
        many: true
```

```yaml
name: github issue data
url: "https://github.com/{url}"
default_url: "https://github.com/microsoft/vscode/issues/170789"
extractors:
  - name: comments
    selector: div.comment
    attributes:
      - name: author
        selector: .author
        attribute: ""
      - name: text
        selector: .comment-body
        attribute: ""
      - name: time
        selector: relative-time.no-wrap
        attribute: datetime
```

```yaml
name: "flow"
flows:
  - task: "github_issues.yaml"
    output: "result.json"
    childs:
      - task: "github_issue.yaml"
        output: "result1.json"
```

# Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvement.


# License
This project is licensed under the MIT License.