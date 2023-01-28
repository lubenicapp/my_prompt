# my_prompt
to print a prompt like i want

call this to try or export in ~/.bashrc:

```bash
export PS1="$(python pwd.py)"
```

It shows 
- virtual env in yellow
- git branch in white
- user@hostname in cyan
- the working directory in blue : /Path/To/Dir => /P/T/Dir
