import asyncio
from helpers import output_processor

class LlmTranslator:
    def __init__(self, llm, system_prompt, collection_delimiters, element_delimiters):
        if collection_delimiters is None:
            raise TypeError("collection_delimiters cannot be None")
        if element_delimiters is None:
            raise TypeError("element_delimiters cannot be None")
        self.llm = llm
        self.system_prompt = system_prompt
        self.collection_delimiters = collection_delimiters
        self.element_delimiters = element_delimiters

    async def __async_list_converter(self, sync_list):
        for item in sync_list:
            yield item

    async def process_batch(self, batch):
        batch_as_string = str(batch.tolist())[1:-1]
        payload = "Input: " + self.element_delimiters[0] + batch_as_string + self.element_delimiters[1]
        messages = [
            ("system", self.system_prompt),
            ("human", payload)
        ]
        response = await self.llm.ainvoke(messages)
        response.content = output_processor.validate_llm_json_output_format(
            response.content,
            self.collection_delimiters[1],
            self.element_delimiters[1]
        )
        return response

    async def process_batches(self, batches_to_process):
        tasks = [self.process_batch(batch) async for batch in self.__async_list_converter(batches_to_process)]
        return await asyncio.gather(*tasks)