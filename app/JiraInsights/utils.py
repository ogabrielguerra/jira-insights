
class Utils:
    
    @staticmethod
    def pymongo_result_to_json(operation, result):
        if operation == 'upsert':
            return {
                'matched': result.matched_count,
                'modified': result.modified_count
            }
        elif operation == 'insert_many':
            num_inserted = len(result.inserted_ids)
            return {
                'inserted_rows': num_inserted
            }
        elif operation == 'insert_one':
            project_id = str(result.inserted_id)
            return {'inserted_id': project_id}

        elif operation == 'upsert_multiple':
            return {'upserted_ids': result}


class DotSyntax(dict):
    __getattr__ = dict.get

