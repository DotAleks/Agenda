from aiogram import BaseMiddleware
from typing import Callable, Dict, Any
import inspect
from aiogram.types import Message

class RepositoryMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        
        from database.repositories import UserRepository
        from database.repositories import TaskRepository
        
        self._repositories = {
            'user_repo': UserRepository,
            'task_repo': TaskRepository,
        }
        
        self._instances_cache = {}
        
        self._handler_signatures = {}
    
    async def __call__(
        self,
        handler: Callable,
        event: Message,
        data: Dict[str, Any]
    ) -> Any:        
        handler_func = data.get('handler')
        if not handler_func:
            return await handler(event, data)
        
        handler_id = id(handler_func)
        if handler_id not in self._handler_signatures:
            self._handler_signatures[handler_id] = self._analyze_handler(handler_func)
        
        param_info = self._handler_signatures[handler_id]
        
        for param_name in param_info['params']:
            repo_class = self._repositories.get(param_name)
            if repo_class:
                if repo_class not in self._instances_cache:
                    self._instances_cache[repo_class] = repo_class()
                
                data[param_name] = self._instances_cache[repo_class]
                break
        
        return await handler(event, data)
    
    def _analyze_handler(self, handler_func: Callable) -> Dict:
        try:
            signature = inspect.signature(handler_func)
            return {
                'params': list(signature.parameters.keys()),
                'has_message': 'message' in signature.parameters,
            }
        except (ValueError, TypeError):
            return {'params': [], 'has_message': False}