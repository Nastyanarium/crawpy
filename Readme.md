# Crawpy

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
python3 main.py flow.yml
```


# Tasks and flow example:

```yaml
name: github issues
url: https://github.com/microsoft/vscode/issues?page={page 2}
extractors:
  - name: issues
    selector: '[class*="IssueRow-module__row"]'
    attributes:
      - name: title
        selector: '[class*="TitleHeader-module"]'
        attribute: ""
      - name: url
        selector: '[class*="TitleHeader-module"]'
        attribute: href
```

```yaml
name: github issue
url: "https://github.com/{url}"
default_url: "https://github.com/microsoft/vscode/issues/170789"
extractors:
  - name: comments
    selector: div[data-testid*="issue-body"],[data-testid*="comment-viewer-outer-box"]
    attributes:
      - name: author
        selector: a[data-testid*="issue-body-header-author"],
          a[data-testid*="avatar-link"]
        attribute: ""
      - name: text
        selector: '[data-testid*="markdown-body"]'
        attribute: ""
      - name: time
        selector: relative-time[datetime]
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
