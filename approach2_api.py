#!/usr/bin/env python3
"""
Approach 2: Modern Async API with FastAPI
Demonstrates OpenClaw's ability to create modern web APIs.
"""

import asyncio
import uvicorn
from datetime import datetime
from typing import Optional, Dict, Any
from enum import Enum

try:
    from fastapi import FastAPI, Query, HTTPException
    from pydantic import BaseModel, Field
    from contextlib import asynccontextmanager
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("FastAPI not installed. Install with: pip install fastapi uvicorn pydantic")


# Data Models
class GreetingFormat(str, Enum):
    """Available greeting formats."""
    SIMPLE = "simple"
    DETAILED = "detailed"
    VERBOSE = "verbose"


class GreetingRequest(BaseModel):
    """Request model for greeting endpoint."""
    name: str = Field(default="World", description="Name to greet")
    format: GreetingFormat = Field(default=GreetingFormat.SIMPLE, description="Greeting format")
    include_timestamp: bool = Field(default=True, description="Include timestamp in response")


class GreetingResponse(BaseModel):
    """Response model for greeting endpoint."""
    greeting: str
    source: str = "OpenClaw"
    timestamp: str
    approach: str = "Modern Async API"
    metadata: Optional[Dict[str, Any]] = None


# FastAPI Application
if HAS_FASTAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        """Lifespan manager for startup/shutdown events."""
        print("🚀 OpenClaw Hello World API starting up...")
        yield
        print("👋 OpenClaw Hello World API shutting down...")
    
    app = FastAPI(
        title="OpenClaw Hello World API",
        description="Modern async API demonstrating OpenClaw's capabilities",
        version="1.0.0",
        lifespan=lifespan
    )
    
    @app.get("/", response_model=GreetingResponse)
    async def root():
        """Root endpoint with default greeting."""
        return await generate_greeting()
    
    @app.get("/hello", response_model=GreetingResponse)
    async def hello(
        name: str = Query(default="World", description="Name to greet"),
        format: GreetingFormat = Query(default=GreetingFormat.SIMPLE, description="Greeting format"),
        include_timestamp: bool = Query(default=True, description="Include timestamp")
    ):
        """Greeting endpoint with customizable parameters."""
        return await generate_greeting(name, format, include_timestamp)
    
    @app.post("/greet", response_model=GreetingResponse)
    async def greet(request: GreetingRequest):
        """Greeting endpoint using POST with request body."""
        return await generate_greeting(
            request.name, 
            request.format, 
            request.include_timestamp
        )
    
    @app.get("/health")
    async def health():
        """Health check endpoint."""
        return {
            "status": "healthy",
            "service": "OpenClaw Hello World API",
            "timestamp": datetime.now().isoformat(),
            "uptime": "0s"  # In production, would calculate actual uptime
        }


# Core Business Logic
async def generate_greeting(
    name: str = "World",
    format: GreetingFormat = GreetingFormat.SIMPLE,
    include_timestamp: bool = True
) -> Dict[str, Any]:
    """Generate greeting based on parameters."""
    timestamp = datetime.now().isoformat() if include_timestamp else None
    
    if format == GreetingFormat.SIMPLE:
        greeting = f"Hello {name}!"
        metadata = None
    elif format == GreetingFormat.DETAILED:
        greeting = f"Hello {name}! Welcome to OpenClaw's demo."
        metadata = {"format": "detailed", "name_length": len(name)}
    elif format == GreetingFormat.VERBOSE:
        greeting = f"Greetings, {name}! This is OpenClaw demonstrating modern API design."
        metadata = {
            "format": "verbose",
            "name_length": len(name),
            "chars": list(name),
            "features": ["async", "typed", "documented", "production_ready"]
        }
    
    return {
        "greeting": greeting,
        "source": "OpenClaw",
        "timestamp": timestamp,
        "approach": "Modern Async API",
        "metadata": metadata
    }


# CLI Interface for testing
async def run_cli_demo():
    """Run a CLI demo of the async greeting generator."""
    print("=== OpenClaw Hello World - Approach 2: Async API Demo ===")
    
    # Test different formats
    test_cases = [
        ("Mykie", GreetingFormat.SIMPLE, True),
        ("OpenClaw", GreetingFormat.DETAILED, True),
        ("World", GreetingFormat.VERBOSE, False),
    ]
    
    for name, fmt, include_ts in test_cases:
        result = await generate_greeting(name, fmt, include_ts)
        print(f"\n📤 Input: name={name}, format={fmt.value}, timestamp={include_ts}")
        print(f"📥 Output: {result['greeting']}")
        if result['metadata']:
            print(f"   Metadata: {result['metadata']}")


def main():
    """Main entry point."""
    if HAS_FASTAPI:
        print("=== OpenClaw Hello World - Approach 2 ===")
        print("This module provides a modern async API with FastAPI.")
        print("\nTo run the API server:")
        print("  uvicorn approach2_api:app --reload --port 8000")
        print("\nAvailable endpoints:")
        print("  GET  /              - Default greeting")
        print("  GET  /hello         - Customizable greeting")
        print("  POST /greet         - Greeting with request body")
        print("  GET  /health        - Health check")
        
        # Run CLI demo
        asyncio.run(run_cli_demo())
    else:
        print("⚠️  FastAPI not installed. This approach requires:")
        print("    pip install fastapi uvicorn pydantic")
        print("\nYou can still use the core logic:")
        asyncio.run(run_cli_demo())


if __name__ == "__main__":
    main()