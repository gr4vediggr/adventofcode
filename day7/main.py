directories = {"/" : {}}

current_dir = directories
last_command = None

class Dir:
    def __init__(self, name) -> None:
        self.name = name
        self.sub_dirs = {}
        self.files = {}
        self.size = 0
        self.changed = False
        self.parent = None

    def get_size(self): 
        child_size = sum([a.get_size() for a in self.sub_dirs.values()])
        file_size = sum([a for a in self.files.values()])
        self.size = file_size + child_size
        self.changed = False
        return self.size

    def add_dir(self, dir_name):
        if dir_name in self.sub_dirs:
            print(f"dir {dir_name} exists in {self.name}")
            return
        new_dir = Dir(dir_name)
        new_dir.parent = self
        self.changed = True

        self.sub_dirs[dir_name] = new_dir

    def add_file(self, file_name, file_size): 
        self.files[file_name] = file_size

    def get_dir(self, dir_name):
        return self.sub_dirs[dir_name]

    def to_str(self, depth = 0): 
        s = " "* depth + self.name + "\n"
        for child in self.sub_dirs.values(): 
            s += child.to_str(depth+1)
        for fname, fsize in self.files.items(): 
            s += " "* depth + " " + fname + ":" + str(fsize) + "\n"
        return s

    def print_dir(self): 
        print(f"DIR({self.name}, size:{self.size})")
        for child in self.sub_dirs.values():
            child.print_dir()


current_dir = Dir('root')
root = current_dir
current_dir.add_dir('/')

sizes = []


    

with open('input.txt') as file:
    lines = file.readlines()

    for line in lines: 
        line = line.strip()

        response = line.split(" ") 

        if response[0] == "$": 
            print("cmd", response[1:])
            last_command= None
            cmd = response[1]
            if cmd == "ls": 
                last_command="ls"
            
            elif cmd == "cd": 
                
                to_dir = response[2]
                if (to_dir == ".."):
                    current_dir = current_dir.parent

                else: 
                    current_dir = current_dir.get_dir(to_dir)

                

        else: 
            if last_command == "ls":

                if response[0] == 'dir': 
                    current_dir.add_dir(response[1])
                else:
                    current_dir.add_file(response[1], int(response[0]))
        
                    
def get_all_below(root_dir, size): 
    result = []


    for child in root_dir.sub_dirs.values(): 
        if child.get_size() <= size:
            result.append((child.name, child.size))
        result += get_all_below(child, size)
    return result
def get_all_above(root_dir, size): 
    result = []


    for child in root_dir.sub_dirs.values(): 
        if child.get_size() >= size:
            result.append((child.name, child.size))
        result += get_all_below(child, size)
    return result

print("part 1 : ", sum( b for _, b in get_all_below(root, 100000)))

current_size = root.get_size()
total_size = 70000000
needed = total_size - current_size
print(needed)
print("current size: ", root.get_size())

all_above = get_all_above(root, needed)
print(sorted(all_above, key = lambda x : x[1]))