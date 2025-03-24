from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        parts = old_node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise Exception(f"Matching closing delimiter '{delimiter}' not found in text")
            
        for i in range(len(parts)):
            part = parts[i]
            if part == "" and i % 2 == 0:
                continue
            if i % 2 == 1:
                new_nodes.append(TextNode(part, text_type))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
                
    return new_nodes
