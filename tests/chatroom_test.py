from llm_task_handler.chatroom import ChatroomConversation
from llm_task_handler.chatroom import ChatroomMessage


def test_to_and_from_yaml() -> None:
    ai_user_id = "2"
    multiline_message = """
These are my favorite things:

- money
- love
- cheeseburgers
"""

    messages = [
        ChatroomMessage(role="2", timestamp=1697086061, content="Hello, how may I help you?"),
        ChatroomMessage(role="1", timestamp=1697086062, content=multiline_message),
        ChatroomMessage(role="2", timestamp=1697086063, content="I see you said " + multiline_message),
    ]

    convo = ChatroomConversation(messages=messages, ai_user_id=ai_user_id)

    yaml_str = convo.to_yaml()

    convo2 = ChatroomConversation.from_yaml(yaml_str)

    assert {m.role for m in messages} == {m.role for m in convo.messages}
    assert {m.role for m in convo.messages} == {m.role for m in convo2.messages}
    assert {m.content for m in convo.messages} == {m.content for m in convo2.messages}
    assert {m.timestamp for m in convo.messages} == {m.timestamp for m in convo2.messages}

    assert convo.ai_user_id == convo2.ai_user_id
