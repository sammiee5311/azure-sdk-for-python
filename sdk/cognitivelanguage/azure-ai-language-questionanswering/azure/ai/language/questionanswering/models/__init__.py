# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AnswerSpan
    from ._models_py3 import AnswersFromTextOptions
    from ._models_py3 import AnswersFromTextResult
    from ._models_py3 import AnswersOptions
    from ._models_py3 import AnswersResult
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse
    from ._models_py3 import InnerErrorModel
    from ._models_py3 import KnowledgeBaseAnswer
    from ._models_py3 import KnowledgeBaseAnswerContext
    from ._models_py3 import KnowledgeBaseAnswerDialog
    from ._models_py3 import KnowledgeBaseAnswerPrompt
    from ._models_py3 import MetadataFilter
    from ._models_py3 import QueryFilters
    from ._models_py3 import ShortAnswerOptions
    from ._models_py3 import TextAnswer
    from ._models_py3 import TextDocument
except (SyntaxError, ImportError):
    from ._models import AnswerSpan  # type: ignore
    from ._models import AnswersFromTextOptions  # type: ignore
    from ._models import AnswersFromTextResult  # type: ignore
    from ._models import AnswersOptions  # type: ignore
    from ._models import AnswersResult  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import InnerErrorModel  # type: ignore
    from ._models import KnowledgeBaseAnswer  # type: ignore
    from ._models import KnowledgeBaseAnswerContext  # type: ignore
    from ._models import KnowledgeBaseAnswerDialog  # type: ignore
    from ._models import KnowledgeBaseAnswerPrompt  # type: ignore
    from ._models import MetadataFilter  # type: ignore
    from ._models import QueryFilters  # type: ignore
    from ._models import ShortAnswerOptions  # type: ignore
    from ._models import TextAnswer  # type: ignore
    from ._models import TextDocument  # type: ignore

from ._question_answering_client_enums import (
    ErrorCode,
    InnerErrorCode,
)

__all__ = [
    "AnswerSpan",
    "AnswersFromTextOptions",
    "AnswersFromTextResult",
    "AnswersOptions",
    "AnswersResult",
    "Error",
    "ErrorResponse",
    "InnerErrorModel",
    "KnowledgeBaseAnswer",
    "KnowledgeBaseAnswerContext",
    "KnowledgeBaseAnswerDialog",
    "KnowledgeBaseAnswerPrompt",
    "MetadataFilter",
    "QueryFilters",
    "ShortAnswerOptions",
    "TextAnswer",
    "TextDocument",
    "ErrorCode",
    "InnerErrorCode",
]
