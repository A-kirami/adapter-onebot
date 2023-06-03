import pytest


@pytest.mark.asyncio
async def test_message_escape():
    from nonebot.adapters.onebot.v11 import Message, MessageSegment

    a = Message([MessageSegment.text("test"), MessageSegment.at(123)])
    assert Message(str(a)) == a

    assert f"{Message()}[CQ:test]" == Message(MessageSegment.text("[CQ:test]"))
    assert f"[CQ:test]{Message()}" == Message(MessageSegment.text("[CQ:test]"))

    a = Message()
    a += "[CQ:test]"
    assert a == Message(MessageSegment.text("[CQ:test]"))

    assert MessageSegment.text("test") + "[CQ:test]" == Message(
        [MessageSegment.text("test"), MessageSegment.text("[CQ:test]")]
    )
    assert "[CQ:test]" + MessageSegment.text("test") == Message(
        [MessageSegment.text("[CQ:test]"), MessageSegment.text("test")]
    )


@pytest.mark.asyncio
async def test_message_rich_expr():
    from nonebot.adapters.onebot.v11 import Message, MessageSegment

    a = MessageSegment.text("[test],test")
    assert a.to_rich_text() == "&#91;test&#93;,test"
    b = MessageSegment.at(123)
    assert b.to_rich_text() == "[at:qq=123]"
