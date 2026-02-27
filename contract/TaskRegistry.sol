// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * TaskRegistry - Onchain Task Verification Contract
 * Bounty #239 - Multi-agent Task Coordination Demo
 * 
 * This contract records task completions from the multi-agent system
 * on the Base blockchain for verification and transparency.
 */

contract TaskRegistry {
    
    // Struct to hold task completion data
    struct TaskRecord {
        bytes32 taskId;
        string topic;
        uint256 timestamp;
        address submitter;
        uint8 agentCount;
        bytes32 verificationHash;
        bool completed;
    }
    
    // State variables
    mapping(bytes32 => TaskRecord) public tasks;
    bytes32[] public allTaskIds;
    
    // Events
    event TaskCompleted(
        bytes32 indexed taskId,
        string topic,
        uint256 timestamp,
        address indexed submitter,
        uint8 agentCount
    );
    
    /**
     * @dev Record a task completion from the multi-agent system
     * @param _topic The topic that was researched/written about
     * @param _agentCount Number of agents that worked on the task
     * @param _verificationHash Hash to verify task integrity
     */
    function recordTaskCompletion(
        string memory _topic,
        uint8 _agentCount,
        bytes32 _verificationHash
    ) public returns (bytes32) {
        // Create unique task ID from topic and timestamp
        bytes32 taskId = keccak256(
            abi.encodePacked(_topic, block.timestamp, _verificationHash)
        );
        
        // Create the task record
        tasks[taskId] = TaskRecord({
            taskId: taskId,
            topic: _topic,
            timestamp: block.timestamp,
            submitter: msg.sender,
            agentCount: _agentCount,
            verificationHash: _verificationHash,
            completed: true
        });
        
        allTaskIds.push(taskId);
        
        // Emit completion event
        emit TaskCompleted(taskId, _topic, block.timestamp, msg.sender, _agentCount);
        
        return taskId;
    }
    
    /**
     * @dev Get task details by ID
     * @param _taskId The task ID to look up
     */
    function getTask(bytes32 _taskId) public view returns (
        string memory topic,
        uint256 timestamp,
        address submitter,
        uint8 agentCount,
        bool completed
    ) {
        TaskRecord memory task = tasks[_taskId];
        return (
            task.topic,
            task.timestamp,
            task.submitter,
            task.agentCount,
            task.completed
        );
    }
    
    /**
     * @dev Get total number of recorded tasks
     */
    function getTaskCount() public view returns (uint256) {
        return allTaskIds.length;
    }
    
    /**
     * @dev Verify a task exists and is completed
     * @param _taskId The task ID to verify
     */
    function verifyTask(bytes32 _taskId) public view returns (bool) {
        return tasks[_taskId].completed;
    }
}