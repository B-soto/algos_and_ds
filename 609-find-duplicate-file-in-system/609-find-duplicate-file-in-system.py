class Solution:
    def get_dups(self, my_dict):
        
        
        return 
        
                
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        seen_dict = {}# word:file
        duplicate_list = []
        
        for path in paths:
            # print(path)
            # print(path.split(' '))
            path_arr = path.split(' ')
            path_dir = path_arr[0]
            path_files = path_arr[1:]
            for file in path_files:
                text = []
                file_name = []
                open_bracket = False                
                for char in file:
                    if char == '(':
                        open_bracket = True
                    if open_bracket:
                        text.append(char)
                    else:
                        file_name.append(char)
                    
                full_file_path = path_dir + '/' + ''.join(file_name)
                text = ''.join(text).strip('()')
                print(full_file_path , "-", text)
                if text not in seen_dict:
                    seen_dict[text] = [full_file_path]
                else:
                    seen_dict[text].append(full_file_path)
            
        # print(seen_dict)

        # answer = self.get_dups(seen_dict)
        return [v for k,v in seen_dict.items() if len(v)>1]
        