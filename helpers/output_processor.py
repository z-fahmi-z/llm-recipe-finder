import json

def validate_llm_json_output_format(output, collection_closure, element_closure):
    if collection_closure is None:
        raise ValueError("collection_closure cannot be None, Hint: fences like }, ]")
    if element_closure is None:
        raise ValueError("element_closure cannot be None, Hint: fences like }, ]")
    try:
        closure_begin_index = len(output) - len(collection_closure)
        if output[closure_begin_index:] != collection_closure:
            refactored = output
            last_unfinished_index = refactored.rfind(element_closure) + 1
            refactored = refactored[:last_unfinished_index] + collection_closure
            return refactored
        return output
    except json.JSONDecodeError as e:
        print(f"Error :{str(e)}")

def parse_llm_outputs_to_json_array(outputs, strip_delimiters):
    if strip_delimiters is None or len(strip_delimiters) != 2:
        raise ValueError("start and end fences required")

    start_fence = strip_delimiters[0]
    end_fence = strip_delimiters[1]
    json_array = []
    for output in outputs:
        try:
            content = output.content.strip(start_fence).strip(end_fence)
            parsed = json.loads(content)
            json_array += parsed
        except json.decoder.JSONDecodeError as e:
            print(f"Failed to decode JSON at line {e.lineno}, column {e.colno}")
            print(f"Error message: {e.msg}")
            line = content.splitlines()[e.lineno - 1]
            print(f"Line: {line}...")
    return json_array