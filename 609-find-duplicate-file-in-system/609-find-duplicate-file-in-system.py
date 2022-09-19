class Solution:
  
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        seen_dict = {}
        
        for path in paths:
           
            path_arr = path.split(' ')
            path_dir = path_arr[0]
            # path_files = path_arr[1:]
            
            for file in path_arr[1:]:
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
                text = ''.join(text)
                
                if text not in seen_dict:
                    seen_dict[text] = [full_file_path]
                else:
                    seen_dict[text].append(full_file_path)

        return [v for k,v in seen_dict.items() if len(v)>1]
        