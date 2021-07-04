import json

class ResponseHandler:
    ERR_TEMPLATE = {
        "errorType": "",
        "errorMessage": ""
    }
    RES_TEMPLATE = {
        "Message": ""
    }

    def __init__(self):
        self.errors = []

    def append_eroor(self, type: str, message: str):
        """返却するエラー内容をセット

        Args:
            type (str): エラータイプ
            message (str): エラーメッセージ
        """
        dic = ResponseHandler.ERR_TEMPLATE.copy()
        dic['errorType'] = type
        dic['errorMessage'] = message
        self.errors.append(dic)

    def get_errors(self) -> str:
        """エラーメッセージの返却

        Returns:
            [str]: JSON形式のエラー内容
        """
        return json.dumps(self.errors)

    def get_respose(self, body: str) -> str:
        """
        レスポンスをJsonで返却
        通常成功時はEC2インスタンスのidをリスト形式で返却

        Args:
            body (str): メッセージ内容

        Returns:
            [str]: Json形式のレスポンス
        """
        dic = ResponseHandler.RES_TEMPLATE.copy()
        dic['Message'] = body
        return json.dumps(dic)
