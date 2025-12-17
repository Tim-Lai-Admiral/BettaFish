# -*- coding: utf-8 -*-
"""
存储数据库连接信息和API密钥
"""

from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field
from pathlib import Path

# 固定使用 MindSpider 目录下的 .env（不再受当前工作目录影响）
PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
ENV_FILE: str = str(Path(__file__).resolve().parent / ".env")

class Settings(BaseSettings):
    """全局配置管理，优先从环境变量和.env加载。支持MySQL/PostgreSQL统一数据库参数命名。"""
    DB_DIALECT: str = Field("mysql", description="数据库类型，支持'mysql'或'postgresql'")
    DB_HOST: str = Field("your_host", description="数据库主机名或IP地址")
    DB_PORT: int = Field(3306, description="数据库端口号")
    DB_USER: str = Field("your_username", description="数据库用户名")
    DB_PASSWORD: str = Field("your_password", description="数据库密码")
    DB_NAME: str = Field("mindspider", description="数据库名称")
    DB_CHARSET: str = Field("utf8mb4", description="数据库字符集")
    MINDSPIDER_API_KEY: Optional[str] = Field(None, description="MINDSPIDER API密钥")
    MINDSPIDER_BASE_URL: Optional[str] = Field("https://api.deepseek.com", description="MINDSPIDER API基础URL，推荐deepseek-chat模型使用https://api.deepseek.com")
    MINDSPIDER_MODEL_NAME: Optional[str] = Field("deepseek-chat", description="MINDSPIDER API模型名称, 推荐deepseek-chat")

    class Config:
        env_file = ENV_FILE
        env_prefix = ""
        case_sensitive = False
        extra = "allow"

settings = Settings()
