from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

ERROR_AUTOMATION_NODE_BEFORE_INVALID = (
    "ERROR_AUTOMATION_NODE_BEFORE_INVALID",
    HTTP_400_BAD_REQUEST,
    "{e}",
)

ERROR_AUTOMATION_NODE_DOES_NOT_EXIST = (
    "ERROR_AUTOMATION_NODE_DOES_NOT_EXIST",
    HTTP_404_NOT_FOUND,
    "The requested node does not exist.",
)

ERROR_AUTOMATION_NODE_NOT_IN_WORKFLOW = (
    "ERROR_AUTOMATION_NODE_NOT_IN_WORKFLOW",
    HTTP_400_BAD_REQUEST,
    "The node id {e.node_id} does not belong to the workflow.",
)
