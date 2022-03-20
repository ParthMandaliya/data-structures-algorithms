class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        self.__length = 0
    
    def add_child(self, children):
        self.__length += len(children)
        for child in children:
            child.parent = self
            self.children.append(child)

    def __len__(self):
        return self.__length

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self, properties, level="DEEPEST"):
        space_levels = self.get_level()
        if level != "DEEPEST" and space_levels > level:
            return
        if level == "DEEPEST":
            level = len(self)+1

        spaces = " " * space_levels * 3
        prefix = spaces + "|__" if space_levels > 0 else ""
        print_this = ""
        if properties == "all":
            properties = list(self.data.keys())
        for property in properties:
            print_this += self.data[property] + " "
        print (prefix + print_this.strip())
        if self.children:
            for child in self.children:
                child.print_tree(properties, level)

if __name__ == "__main__":
    root = TreeNode(data={"name": "Nilpul", "designation": "(CEO)"})

    cto = TreeNode(data={"name": "Chinmay", "designation": "(CTO)"})

    it_head = TreeNode(data={"name": "Vishwa", "designation": "(Infrastructure Head)"})
    it_head.add_child([
        TreeNode(data={"name": "Dhaval", "designation": "(Cloud Manager)"}),
        TreeNode(data={"name": "Abhijit", "designation": "(App Manager)"}),
    ])
    app_head = TreeNode(data={"name": "Aamir", "designation": "(Application Head)"})

    cto.add_child([it_head, app_head])

    hr_head = TreeNode(data={"name": "Gels", "designation": "(HR Head)"})
    hr_head.add_child([
        TreeNode(data={"name": "Peter", "designation": "(Recruitment Manager)"}),
        TreeNode(data={"name": "George", "designation": "(Policy Manager)"}),
    ])

    root.add_child([cto, hr_head])

    print ("-"*20+"all"+"-"*20)
    root.print_tree("all")

    print ("-"*20+"name"+"-"*20)
    root.print_tree(("name",))
    
    print ("-"*20+"designation"+"-"*20)
    root.print_tree(("designation",))
    
    print ("-"*20+"name, designation"+"-"*20)
    root.print_tree(("name", "designation"))
    
    print ("-"*20+"name, level=0"+"-"*20)
    root.print_tree("all", level=0)

    print ("-"*20+"name, level=1"+"-"*20)
    root.print_tree("all", level=1)

    print ("-"*20+"name, level=2"+"-"*20)
    root.print_tree("all", level=2)
    
    print ("-"*20+"name, level=3"+"-"*20)
    root.print_tree("all", level=3)
