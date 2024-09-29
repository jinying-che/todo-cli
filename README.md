# todo-cli

## Test 
```bash
# use venv
python3 -m venv venv
../venv/bin/activate
# run the command
python3 todo.py --help
```

## Functions 
- create a todo task 
- update the task status
- list the todo tasks
- tag system
- search the todo task by tag or status

## Tech Design
1. Storage:
    - use the file system to store the data
    - location: `~/.config/todo-cli/db/title_time_xx.md` (store the data by day)
2. Data Structure:
    - task meta data: 
        - title
        - status
        - tags
        - create time
        - update time
3. UX: 
    - list the title of the tasks
    - able to edit the detail of the task 
