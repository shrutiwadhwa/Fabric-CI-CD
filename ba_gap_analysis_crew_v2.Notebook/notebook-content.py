# Fabric notebook source


# CELL ********************

import os
from typing import Any, List, Union
from typing import Literal
from typing import Optional

from datascape.utils.functions import load_yaml
from crewai import Agent, Task, Crew, Process
from datascape.config.secrets import bootstrap_config
from pydantic import BaseModel

from src.datascape.tools.knowledge_base_tool import KnowledgeBaseTool
from src.datascape.tools.knowledge_base_tool_v2 import KnowledgeBaseToolV2
from datascape.tools.vector_store_retrieval_tool import VectorStoreRetrievalTool

bootstrap_config()


class BAKnowledgeSourceCrew:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_knowledge_source_agents.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_knowledge_source_tasks.yaml')

    def crew(self) -> Crew:
        data_engineering_knowledge_retriever = Agent(
            config=self.agents_config['data_engineering_knowledge_retriever'],
            tools=[KnowledgeBaseTool()]
        )

        retrieve_data_engineering_knowledge = Task(
            config=self.tasks_config['retrieve_data_engineering_knowledge'],
            agent=data_engineering_knowledge_retriever
        )

        knowledge_filter = Agent(
            config=self.agents_config['knowledge_filter']
        )

        filter_knowledge = Task(
            config=self.tasks_config['filter_knowledge'],
            agent=knowledge_filter
        )

        return Crew(
            agents=[data_engineering_knowledge_retriever, knowledge_filter],
            tasks=[retrieve_data_engineering_knowledge, filter_knowledge],
            process=Process.sequential,
            memory=False,
            verbose=True
        )


class BAKnowledgeSourceCrewV2:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_knowledge_source_agents_v2.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_knowledge_source_tasks_v2.yaml')

    def crew(self) -> Crew:
        data_engineering_knowledge_retriever = Agent(
            config=self.agents_config['data_engineering_knowledge_retriever'],
            tools=[KnowledgeBaseToolV2()]
        )

        retrieve_data_engineering_knowledge = Task(
            config=self.tasks_config['retrieve_data_engineering_knowledge_v2'],
            agent=data_engineering_knowledge_retriever
        )

        return Crew(
            agents=[data_engineering_knowledge_retriever],
            tasks=[retrieve_data_engineering_knowledge],
            process=Process.sequential,
            memory=False,
            verbose=True
        )


class Source(BaseModel):
    document: str
    statement: str
    context: str


class Conflict(BaseModel):
    type: Literal["Conflict"]  # "Conflict"
    id: int
    change_type: str
    summary: str
    sources: List[Source]


class Conflicts(BaseModel):
    conflicts_and_contradictions: List[Conflict]


class BAConflictDetectionCrewV2:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_conflict_detection_agents_v2.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_conflict_detection_tasks_v2.yaml')

    def crew(self) -> Crew:
        requirements_conflict_detector = Agent(
            config=self.agents_config['requirements_conflict_detector']
        )

        detect_requirements_conflicts = Task(
            config=self.tasks_config['detect_requirements_conflicts'],
            agent=requirements_conflict_detector
        )

        conflict_reviewer = Agent(
            config=self.agents_config['conflict_reviewer']
        )

        review_conflict_report = Task(
            config=self.tasks_config['review_conflict_report'],
            agent=conflict_reviewer,
            output_json=Conflicts
        )

        return Crew(
            agents=[requirements_conflict_detector, conflict_reviewer],
            tasks=[detect_requirements_conflicts, review_conflict_report],
            process=Process.sequential,
            memory=False,
            verbose=True
        )

class BAConflictDeciderCrew:
    def __init__(self):
        self.agents_config = load_yaml('src/datascape/config/requirement_analysis/gap_analysis_conflict_decider_agents.yaml')
        self.tasks_config = load_yaml('src/datascape/config/requirement_analysis/gap_analysis_conflict_decider_tasks.yaml')

    def crew(self) -> Crew:
        conflict_decider = Agent(
            config=self.agents_config['conflict_decider']
        )

        decide_conflict_status = Task(
            config=self.tasks_config['decide_conflict_status'],
            agent=conflict_decider,
            output_json=Conflicts
        )

        return Crew(
            agents=[conflict_decider],
            tasks=[decide_conflict_status],
            process=Process.sequential,
            memory=False,
            verbose=True
        )


class Recommendation(BaseModel):
    type: Literal["Recommendation"]  # "Recommendation"
    id: int
    change_type: str
    configuration_name: str
    justification: str
    expected_value: Any
    use_case: str


class Recommendations(BaseModel):
    recommended_enhancements: List[Recommendation]


class BAConfigurationRecommenderCrewV2:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_configuration_recommender_agents_v2.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_configuration_recommender_tasks_v2.yaml')

    def crew(self) -> Crew:
        configuration_recommender = Agent(
            config=self.agents_config['configuration_recommender']
        )

        recommend_configurations = Task(
            config=self.tasks_config['recommend_configurations'],
            agent=configuration_recommender,
            output_json=Recommendations
        )

        return Crew(
            agents=[configuration_recommender],
            tasks=[recommend_configurations],
            process=Process.sequential,
            memory=False,
            verbose=True
        )

class BARecommendationDeciderCrew:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_recommendation_decider_agents.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_recommendation_decider_tasks.yaml')

    def crew(self) -> Crew:
        configuration_recommendation_decider = Agent(
            config=self.agents_config['configuration_recommendation_decider']
        )

        decide_configuration_recommendations = Task(
            config=self.tasks_config['decide_configuration_recommendations'],
            agent=configuration_recommendation_decider,
            output_json=Recommendations
        )

        return Crew(
            agents=[configuration_recommendation_decider],
            tasks=[decide_configuration_recommendations],
            process=Process.sequential,
            memory=False,
            verbose=True
        )

class MissingConfiguration(BaseModel):
    type: Literal["Missing Configuration"]  # "Missing Configuration"
    id: int
    change_type: str
    configuration_name: str
    description: str
    impact: str
    expected_configuration: Any


class MissingConfigurations(BaseModel):
    missing_mandatory_configurations: List[MissingConfiguration]


class BAConfigurationCompletorCrewV2:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_configuration_completor_agents_v2.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_configuration_completor_tasks_v2.yaml')

    def crew(self) -> Crew:
        configuration_completeness_checker = Agent(
            config=self.agents_config['configuration_completeness_checker'],
        )

        check_configuration_completeness = Task(
            config=self.tasks_config['check_configuration_completeness'],
            agent=configuration_completeness_checker,
            output_json=MissingConfigurations
        )

        return Crew(
            agents=[configuration_completeness_checker],
            tasks=[check_configuration_completeness],
            process=Process.sequential,
            memory=False,
            verbose=True
        )

class BAConfigurationCompletionDeciderCrew:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_configuration_completor_decider_agents.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_configuration_completor_decider_tasks.yaml')

    def crew(self) -> Crew:
        configuration_completeness_decider = Agent(
            config=self.agents_config['configuration_completeness_decider'],
        )

        decide_configuration_completeness = Task(
            config=self.tasks_config['decide_configuration_completeness'],
            agent=configuration_completeness_decider,
            output_json=MissingConfigurations
        )

        return Crew(
            agents=[configuration_completeness_decider],
            tasks=[decide_configuration_completeness],
            process=Process.sequential,
            memory=False,
            verbose=True
        )

class RequirementsGapSummary(BaseModel):
    conflicts_and_contradictions: List[Conflict] = []
    missing_mandatory_configurations: List[MissingConfiguration] = []
    recommended_enhancements: List[Recommendation] = []


class RequirementsGapSummaryOutput(BaseModel):
    extracted_requirements: Any
    requirements_gap_summary: RequirementsGapSummary


# Build the Gap Summary output by aggregating various gaps
def create_gap_summary_v2(
        requirements: Any,
        conflicts: Union[List[Conflict], dict],
        missing: Union[List[MissingConfiguration], dict],
        recommendations: Union[List[Recommendation], dict]
) -> RequirementsGapSummaryOutput:
    if isinstance(conflicts, dict):
        conflicts = Conflicts(**conflicts).conflicts_and_contradictions

    if isinstance(missing, dict):
        missing = MissingConfigurations(**missing).missing_mandatory_configurations

    if isinstance(recommendations, dict):
        recommendations = Recommendations(**recommendations).recommended_enhancements

    return RequirementsGapSummaryOutput(
        extracted_requirements=requirements,
        requirements_gap_summary=RequirementsGapSummary(
            conflicts_and_contradictions=conflicts,
            missing_mandatory_configurations=missing,
            recommended_enhancements=recommendations
        )
    )


class Technology(BaseModel):
    source: Optional[List[str]] = None
    processing_technology: Optional[List[str]] = None
    target: Optional[List[str]] = None
    platform: Optional[List[str]] = None
    orchestration_framework: Optional[List[str]] = None


class TechnologyCheckResult(BaseModel):
    status: bool
    technology: Optional[Technology] = None
    extracted_requirements: Optional[Any] = None
    requirements_gap_summary: Optional[RequirementsGapSummary] = None


class BATechStackCheckerCrew:
    def __init__(self, project_name, documents, stage):
        self.project_name = project_name
        self.documents = documents
        self.stage = stage
        if stage.lower() == 'pipeline':
            self.agents_config = load_yaml('src/datascape/config/requirement_analysis/tech_stack_checker_pipeline_agents.yaml')
            self.tasks_config = load_yaml('src/datascape/config/requirement_analysis/tech_stack_checker_pipeline_tasks.yaml')
        else:
            self.agents_config = load_yaml('src/datascape/config/requirement_analysis/tech_stack_checker_agents.yaml')
            self.tasks_config = load_yaml('src/datascape/config/requirement_analysis/tech_stack_checker_tasks.yaml')

    def crew(self) -> Crew:
        data_stack_validator = Agent(
            config=self.agents_config['data_stack_validator'],
            tools=[VectorStoreRetrievalTool(
                project_name=self.project_name,
                sources=self.documents,
                include_metadata=True
            )]
        )

        validate_data_stack = Task(
            config=self.tasks_config['validate_data_stack'],
            agent=data_stack_validator,
            output_json=TechnologyCheckResult
        )

        return Crew(
            agents=[data_stack_validator],
            tasks=[validate_data_stack],
            process=Process.sequential,
            verbose=True
        )


class BATechSpecBuilderCrewV2:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_tech_spec_builder_agents_v2.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_tech_spec_builder_tasks_v2.yaml')

    def crew(self) -> Crew:
        data_architect = Agent(
            config=self.agents_config['data_architect']
        )

        build_data_engineering_spec = Task(
            config=self.tasks_config['build_data_engineering_spec'],
            agent=data_architect,
        )

        return Crew(
            agents=[data_architect],
            tasks=[build_data_engineering_spec],
            process=Process.sequential,
            verbose=True
        )


class BATechSpecBuilderCrew:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_tech_spec_builder_agents.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_tech_spec_builder_tasks.yaml')

    def crew(self) -> Crew:
        data_architect = Agent(
            config=self.agents_config['data_architect']
        )

        build_data_engineering_spec = Task(
            config=self.tasks_config['build_data_engineering_spec'],
            agent=data_architect,
        )

        return Crew(
            agents=[data_architect],
            tasks=[build_data_engineering_spec],
            process=Process.sequential,
            verbose=True
        )

class BARequirementMapperCrew:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_requirement_mapper_agents.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_requirement_mapper_tasks.yaml')

    def crew(self) -> Crew:
        requirement_mapper = Agent(
            config=self.agents_config['requirement_mapper'],
        )

        map_brd_to_template = Task(
            config=self.tasks_config['map_brd_to_template'],
            agent=requirement_mapper
        )

        return Crew(
            agents=[requirement_mapper],
            tasks=[map_brd_to_template],
            process=Process.sequential,
            memory=False,
            verbose=True
        )


class BATemplateMapperCrew:
    def __init__(self):
        self.agents_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_template_mapper_agents.yaml')
        self.tasks_config = load_yaml(
            'src/datascape/config/requirement_analysis/gap_analysis_template_mapper_tasks.yaml')

    def crew(self) -> Crew:
        template_technical_mapper = Agent(
            config=self.agents_config['template_technical_mapper'],
        )

        map_technical_details = Task(
            config=self.tasks_config['map_technical_details'],
            agent=template_technical_mapper
        )

        return Crew(
            agents=[template_technical_mapper],
            tasks=[map_technical_details],
            process=Process.sequential,
            memory=False,
            verbose=True
        )
