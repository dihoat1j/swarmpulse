from abc import ABC, abstractmethod
from typing import List

class GameEngineDriver(ABC):
    @abstractmethod
    def inject_script(self, script_body: str) -> bool:
        pass

    @abstractmethod
    def get_logs(self) -> List[str]:
        pass

class UnityDriver(GameEngineDriver):
    def inject_script(self, script_body: str) -> bool:
        # Mocking C# script injection
        return "[Unity] Script injected successfully"

    def get_logs(self) -> List[str]:
        return ["NullReferenceException at PlayerController.cs:42"]

class UnrealDriver(GameEngineDriver):
    def inject_script(self, script_body: str) -> bool:
        # Mocking C++ snippet injection
        return "[Unreal] Actor spawn logic updated"
    
    def get_logs(self) -> List[str]:
        return ["LogStreaming: Error: Failed to find object"]
